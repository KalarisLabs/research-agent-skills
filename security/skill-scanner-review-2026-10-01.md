# Skill scanner review — 2026-10-01

The 53 new HIGH findings in the 281-skill scan map to 50 unique skill, rule, and relative-file keys. Each was reviewed before baseline acceptance. Eight agent-facing calculator examples that used Python `eval()` were replaced with bounded arithmetic parsers and are excluded here. The scanner gate still fails on new keys.

| Finding key | Review |
| --- | --- |
| `autoskill|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | Provider keys go to selected endpoints; Screenpipe token goes to configured daemon. Remote cleartext endpoints are rejected. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `autoskill|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | Provider keys go to selected endpoints; Screenpipe token goes to configured daemon. Remote cleartext endpoints are rejected. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `autoskill|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/backends.py` | Provider keys go to selected endpoints; Screenpipe token goes to configured daemon. Remote cleartext endpoints are rejected. |
| `autoskill|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/doctor.py` | Provider keys go to selected endpoints; Screenpipe token goes to configured daemon. Remote cleartext endpoints are rejected. |
| `autoskill|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/run.py` | Provider keys go to selected endpoints; Screenpipe token goes to configured daemon. Remote cleartext endpoints are rejected. |
| `citation-management|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | NCBI_API_KEY and NCBI_EMAIL go to fixed NCBI endpoints; other citation lookups use public APIs. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `citation-management|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | NCBI_API_KEY and NCBI_EMAIL go to fixed NCBI endpoints; other citation lookups use public APIs. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `citation-management|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/extract_metadata.py` | NCBI_API_KEY and NCBI_EMAIL go to fixed NCBI endpoints; other citation lookups use public APIs. |
| `citation-management|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/search_pubmed.py` | NCBI_API_KEY and NCBI_EMAIL go to fixed NCBI endpoints; other citation lookups use public APIs. |
| `geomaster|MDBLOCK_PYTHON_EVAL_EXEC|references/machine-learning.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `histolab|MDBLOCK_PYTHON_EVAL_EXEC|references/filters_preprocessing.md` | Comment mentions an OpenCV constant and Python eval; no execution occurs. |
| `implementing-llms-litgpt|MDBLOCK_PYTHON_EVAL_EXEC|references/custom-models.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `infographics|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `infographics|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `infographics|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_infographic_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. |
| `langsmith-observability|MDBLOCK_PYTHON_EVAL_EXEC|references/advanced-usage.md` | Function name contains eval; no dynamic execution occurs. |
| `latex-posters|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `latex-posters|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `latex-posters|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_schematic_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. |
| `literature-review|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API; citation lookup uses publication APIs. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `literature-review|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API; citation lookup uses publication APIs. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `literature-review|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_schematic_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API; citation lookup uses publication APIs. |
| `long-context|MDBLOCK_PYTHON_EVAL_EXEC|references/fine_tuning.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `modal-serverless-gpu|MDBLOCK_PYTHON_EVAL_EXEC|references/advanced-usage.md` | Constant print command runs inside an isolated sandbox; no agent input is executed. |
| `modal|MDBLOCK_PYTHON_EVAL_EXEC|references/functions.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `model-merging|MDBLOCK_PYTHON_EVAL_EXEC|references/coefficient-tuning.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `model-merging|MDBLOCK_PYTHON_EVAL_EXEC|references/evaluation.md` | Function name contains eval; no dynamic execution occurs. |
| `model-pruning|MDBLOCK_PYTHON_EVAL_EXEC|references/wanda.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `model-pruning|MDBLOCK_PYTHON_EVAL_EXEC|skill.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `nanogpt|MDBLOCK_PYTHON_EVAL_EXEC|references/training.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `prompt-guard|MDBLOCK_PYTHON_EVAL_EXEC|skill.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `pytorch-lightning-distributed|MDBLOCK_PYTHON_EVAL_EXEC|references/distributed.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `research-lookup|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | PARALLEL_API_KEY and OPENROUTER_API_KEY go to explicitly selected HTTPS research providers. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `research-lookup|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | PARALLEL_API_KEY and OPENROUTER_API_KEY go to explicitly selected HTTPS research providers. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `research-lookup|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/research_lookup.py` | PARALLEL_API_KEY and OPENROUTER_API_KEY go to explicitly selected HTTPS research providers. |
| `scientific-schematics|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `scientific-schematics|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `scientific-schematics|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_schematic_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. |
| `scientific-slides|BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `scientific-slides|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. Cross-file alert has an invalid bundled rule contract and shows no unauthorized destination. |
| `scientific-slides|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_schematic_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. |
| `scientific-slides|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/generate_slide_image_ai.py` | OPENROUTER_API_KEY goes to fixed HTTPS OpenRouter image API. |
| `segment-anything-model|MDBLOCK_PYTHON_EVAL_EXEC|references/advanced-usage.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `tensorboard|MDBLOCK_PYTHON_EVAL_EXEC|references/integration-examples.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `tensorboard|MDBLOCK_PYTHON_EVAL_EXEC|references/profiling.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `tensorboard|MDBLOCK_PYTHON_EVAL_EXEC|references/visualization.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `waypoint-bio|MDBLOCK_PYTHON_EVAL_EXEC|references/python-api.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `weights-and-biases|MDBLOCK_PYTHON_EVAL_EXEC|references/artifacts.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `weights-and-biases|MDBLOCK_PYTHON_EVAL_EXEC|references/integrations.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
| `weights-and-biases|MDBLOCK_PYTHON_EVAL_EXEC|references/sweeps.md` | Model.eval() switches a model to inference mode; it is not Python dynamic execution. |
