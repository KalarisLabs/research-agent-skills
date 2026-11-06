/**
 * Research Agent Skills · Interactive Searchable Web Catalog
 * Client-side fast search and filtering engine.
 */

(function () {
  "use strict";

  const REPO_BASE = "https://github.com/KalarisLabs/research-agent-skills";

  // State
  let catalogData = { skills: [], categories: [], bundles: {} };
  let currentSearch = "";
  let currentCategory = "all";
  let currentBundle = "all";

  // DOM Elements
  const searchInput = document.getElementById("searchInput");
  const bundleSelector = document.getElementById("bundleSelector");
  const categoryList = document.getElementById("categoryList");
  const skillsGrid = document.getElementById("skillsGrid");
  const resultsCount = document.getElementById("resultsCount");
  const activeFilterLabel = document.getElementById("activeFilterLabel");
  const metricCount = document.getElementById("metricCount");
  const themeToggle = document.getElementById("themeToggle");
  const sunIcon = document.getElementById("sunIcon");
  const moonIcon = document.getElementById("moonIcon");
  const toast = document.getElementById("toast");
  const toastMessage = document.getElementById("toastMessage");

  // Modal Elements
  const detailModal = document.getElementById("detailModal");
  const modalSkillName = document.getElementById("modalSkillName");
  const modalSkillDesc = document.getElementById("modalSkillDesc");
  const modalSkillCategory = document.getElementById("modalSkillCategory");
  const modalSkillVersion = document.getElementById("modalSkillVersion");
  const modalSkillCompat = document.getElementById("modalSkillCompat");
  const modalSkillTags = document.getElementById("modalSkillTags");
  const modalGitHubLink = document.getElementById("modalGitHubLink");
  const modalCloseBtn = document.getElementById("modalCloseBtn");
  const cmdSkillsSh = document.getElementById("cmdSkillsSh");
  const cmdUvx = document.getElementById("cmdUvx");
  const cmdClaude = document.getElementById("cmdClaude");
  const btnCopySkillsSh = document.getElementById("btnCopySkillsSh");
  const btnCopyUvx = document.getElementById("btnCopyUvx");
  const btnCopyClaude = document.getElementById("btnCopyClaude");

  // Theme Management
  function initTheme() {
    const saved = localStorage.getItem("ras_theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    setTheme(saved);
  }

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("ras_theme", theme);
    if (theme === "dark") {
      sunIcon.style.display = "block";
      moonIcon.style.display = "none";
    } else {
      sunIcon.style.display = "none";
      moonIcon.style.display = "block";
    }
  }

  themeToggle.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") || "light";
    setTheme(cur === "dark" ? "light" : "dark");
  });

  // Toast Helper
  let toastTimer = null;
  function showToast(text) {
    toastMessage.textContent = text;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove("show");
    }, 2200);
  }

  // Clipboard Copy Helper
  function copyToClipboard(text, btnElement) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(`Copied: ${text}`);
      if (btnElement) {
        const originalText = btnElement.textContent;
        btnElement.textContent = "Copied!";
        btnElement.classList.add("copied");
        setTimeout(() => {
          btnElement.textContent = originalText;
          btnElement.classList.remove("copied");
        }, 1800);
      }
    }).catch(() => {
      showToast("Failed to copy to clipboard");
    });
  }

  // Fetch Catalog
  async function loadCatalog() {
    try {
      const response = await fetch("skills.json");
      if (!response.ok) throw new Error("Failed to load skills.json");
      catalogData = await response.json();
      initUI();
    } catch (err) {
      console.warn("skills.json fetch failed, loading fallback data...", err);
      // Attempt loading parent catalog
      try {
        const fallback = await fetch("../catalog/skills.json");
        catalogData = await fallback.json();
        initUI();
      } catch (err2) {
        skillsGrid.innerHTML = `<div style="text-align:center; padding: 3rem; color: var(--text-muted);">
          Failed to load catalog data. Please ensure skills.json is present.
        </div>`;
      }
    }
  }

  function initUI() {
    if (metricCount && catalogData.skills) {
      metricCount.textContent = catalogData.skills.length;
    }
    renderCategories();
    renderSkills();
    handleHashNavigation();
  }

  function renderCategories() {
    const cats = catalogData.categories || [];
    let html = `
      <button class="category-chip ${currentCategory === 'all' ? 'active' : ''}" data-cat="all">
        All Categories
        <span class="chip-count">${catalogData.skills.length}</span>
      </button>
    `;
    cats.forEach(c => {
      html += `
        <button class="category-chip ${currentCategory === c.id ? 'active' : ''}" data-cat="${escapeHtml(c.id)}">
          ${escapeHtml(formatCategoryName(c.id))}
          <span class="chip-count">${c.count}</span>
        </button>
      `;
    });
    categoryList.innerHTML = html;

    categoryList.querySelectorAll(".category-chip").forEach(btn => {
      btn.addEventListener("click", () => {
        categoryList.querySelectorAll(".category-chip").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentCategory = btn.dataset.cat;
        renderSkills();
      });
    });
  }

  function formatCategoryName(id) {
    return id.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
  }

  function escapeHtml(str) {
    if (!str) return "";
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Filter Logic
  function getFilteredSkills() {
    let list = catalogData.skills || [];

    // Bundle filter
    if (currentBundle !== "all" && catalogData.bundles) {
      const bundle = catalogData.bundles[currentBundle];
      if (bundle) {
        const bundleCats = new Set(bundle.categories || []);
        const bundleSkills = new Set(bundle.skills || []);
        list = list.filter(s => bundleCats.has(s.category) || bundleSkills.has(s.name));
      }
    }

    // Category filter
    if (currentCategory !== "all") {
      list = list.filter(s => s.category === currentCategory);
    }

    // Search query
    const q = currentSearch.toLowerCase().trim();
    if (q) {
      list = list.filter(s => {
        return (
          s.name.toLowerCase().includes(q) ||
          s.description.toLowerCase().includes(q) ||
          s.category.toLowerCase().includes(q) ||
          (s.tags && s.tags.some(t => t.toLowerCase().includes(q)))
        );
      });
    }

    return list;
  }

  function renderSkills() {
    const list = getFilteredSkills();
    resultsCount.textContent = `Showing ${list.length} skill${list.length === 1 ? '' : 's'}`;

    let label = currentCategory === "all" ? "All Categories" : formatCategoryName(currentCategory);
    if (currentBundle !== "all") {
      label += ` · Bundle: ${currentBundle}`;
    }
    if (currentSearch) {
      label += ` · Matching "${currentSearch}"`;
    }
    activeFilterLabel.textContent = label;

    if (list.length === 0) {
      skillsGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--text-muted);">
          <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🔍</div>
          <h3 style="font-size: 1.25rem; color: var(--text-main); margin-bottom: 0.5rem;">No skills found</h3>
          <p>Try searching for a different keyword or select another category.</p>
        </div>
      `;
      return;
    }

    let cardsHtml = "";
    list.forEach(skill => {
      const skillsShCmd = `npx skills add KalarisLabs/research-agent-skills --skill ${skill.name}`;
      const tags = (skill.tags || []).slice(0, 3).map(t => `<span class="card-tag">#${escapeHtml(t)}</span>`).join("");

      cardsHtml += `
        <div class="skill-card" data-skill-name="${escapeHtml(skill.name)}">
          <div class="card-header">
            <button class="skill-title-btn" data-open-skill="${escapeHtml(skill.name)}">
              ${escapeHtml(skill.name)}
            </button>
            <span class="skill-category-badge">${escapeHtml(skill.category)}</span>
          </div>

          <p class="skill-description">${escapeHtml(skill.description)}</p>

          ${tags ? `<div class="card-tags">${tags}</div>` : ''}

          <div class="card-actions">
            <div class="command-box" title="${escapeHtml(skillsShCmd)}">
              <span class="command-text">${escapeHtml(skillsShCmd)}</span>
              <button class="copy-btn" data-copy="${escapeHtml(skillsShCmd)}">Copy</button>
            </div>

            <div class="card-footer-buttons">
              <button class="inspect-btn" data-open-skill="${escapeHtml(skill.name)}">Inspect Playbook &rarr;</button>
              <a href="${REPO_BASE}/tree/main/skills/${encodeURIComponent(skill.name)}" target="_blank" rel="noopener" class="github-link">
                GitHub
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      `;
    });

    skillsGrid.innerHTML = cardsHtml;
  }

  // Event delegation: values travel in data-* attributes, never inside inline JavaScript.
  skillsGrid.addEventListener("click", (e) => {
    const target = e.target instanceof Element ? e.target : null;
    if (!target) return;
    const copyBtn = target.closest("[data-copy]");
    if (copyBtn) {
      copyToClipboard(copyBtn.getAttribute("data-copy"), copyBtn);
      return;
    }
    const openBtn = target.closest("[data-open-skill]");
    if (openBtn) openSkillModal(openBtn.getAttribute("data-open-skill"));
  });

  function openSkillModal(skillName) {
    const skill = catalogData.skills.find(s => s.name === skillName);
    if (!skill) return;

    modalSkillName.textContent = skill.name;
    modalSkillDesc.textContent = skill.description;
    modalSkillCategory.textContent = skill.category;
    modalSkillVersion.textContent = `v${skill.version || '1.0'}`;
    modalSkillCompat.textContent = skill.compatibility || "Standard Agent Skills compatible";
    modalSkillTags.textContent = (skill.tags && skill.tags.length > 0) ? skill.tags.join(", ") : "None";
    modalGitHubLink.href = `${REPO_BASE}/blob/main/skills/${encodeURIComponent(skill.name)}/SKILL.md`;

    // Install command variations
    const skillsSh = `npx skills add KalarisLabs/research-agent-skills --skill ${skill.name}`;
    const uvx = `uvx research-agent-skills install ${skill.name}`;
    const claude = `/plugin install ${skill.name}@research-agent-skills`;

    cmdSkillsSh.textContent = skillsSh;
    cmdUvx.textContent = uvx;
    cmdClaude.textContent = claude;

    btnCopySkillsSh.onclick = () => copyToClipboard(skillsSh, btnCopySkillsSh);
    btnCopyUvx.onclick = () => copyToClipboard(uvx, btnCopyUvx);
    btnCopyClaude.onclick = () => copyToClipboard(claude, btnCopyClaude);

    detailModal.classList.add("active");
    detailModal.setAttribute("aria-hidden", "false");
    window.location.hash = encodeURIComponent(skill.name);
  }

  function closeModal() {
    detailModal.classList.remove("active");
    detailModal.setAttribute("aria-hidden", "true");
    if (window.location.hash) {
      history.pushState("", document.title, window.location.pathname + window.location.search);
    }
  }

  modalCloseBtn.addEventListener("click", closeModal);
  detailModal.addEventListener("click", (e) => {
    if (e.target === detailModal) closeModal();
  });

  // Bundle Selector
  bundleSelector.querySelectorAll(".bundle-tab").forEach(btn => {
    btn.addEventListener("click", () => {
      bundleSelector.querySelectorAll(".bundle-tab").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentBundle = btn.dataset.bundle;
      renderSkills();
    });
  });

  // Search Input Debounced
  let searchDebounce = null;
  searchInput.addEventListener("input", (e) => {
    clearTimeout(searchDebounce);
    searchDebounce = setTimeout(() => {
      currentSearch = e.target.value;
      renderSkills();
    }, 80);
  });

  // Keyboard Navigation
  window.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
    if (e.key === "Escape") {
      closeModal();
    }
  });

  // Deep Link Navigation via Hash
  function handleHashNavigation() {
    let hash = window.location.hash.replace("#", "").trim();
    try { hash = decodeURIComponent(hash); } catch (_) { return; }
    if (hash && catalogData.skills) {
      const match = catalogData.skills.find(s => s.name === hash);
      if (match) {
        openSkillModal(match.name);
      }
    }
  }

  window.addEventListener("hashchange", handleHashNavigation);

  // Initialize
  initTheme();
  loadCatalog();
})();

