# WLM-Agent — License Overview
This repository contains **two distinct layers**, each governed by a different license:

---

# 1. Shadow Layer (Structural Content)
**Licensed under: WLM Shadow Layer License 1.0 (Final Freeze)**  
**Date: 10 February 2026**

The following directories contain **non-executable structural content**, including prompts, schemas, conceptual frameworks, role definitions, routing logic descriptions, and any other materials that describe the architecture or behavior of WLM-Agent without providing runnable code.

These directories are covered by the **Shadow Layer License**:

- `/prompts/`
- `/schemas/`
- `/examples/`
- `/ALIGNMENT_NOTICE.MD`

Shadow Layer content is:

- **Readable**
- **Citable**
- **Research-usable**

But strictly **not implementable**, **not trainable**, **not derivable**, and **not commercializable**.

For full terms, see:  
`LICENSE.SHADOW_LAYER.md`

---

# 2. Implementation Layer (Executable Code)
**Licensed under: MIT License**  
**Date: 10 February 2026**

The following directories contain **executable code**, runtime logic, integration code, and tests:

- `/src/`
- `/tests/`

This code is open-source and may be:

- Used  
- Modified  
- Distributed  
- Integrated  
- Commercialized  

under the terms of the MIT License.

For full terms, see:  
`LICENSE.CODE.md`

---

# 3. License Boundary Summary

| Directory / File              | License Type                 |
|------------------------------|------------------------------|
| `/prompts/`                  | Shadow Layer License 1.0     |
| `/schemas/`                  | Shadow Layer License 1.0     |
| `/examples/`                 | Shadow Layer License 1.0     |
| `/ALIGNMENT_NOTICE.MD`       | Shadow Layer License 1.0     |
| `/src/`                      | MIT License                  |
| `/tests/`                    | MIT License                  |
| `README.md`                  | MIT (unless structural content is added) |
| `pyproject.toml`             | MIT                          |
| `setup.cfg`                  | MIT                          |

---

# 4. Purpose of the Dual-License Structure
WLM-Agent contains:

- **Structural components** (Shadow Layer)  
- **Executable components** (MIT)

To protect the WLM protocol while enabling open-source agent tooling, the repository uses a **dual-license model**:

- **Shadow Layer = protected, non-operational, non-derivable**  
- **Code Layer = open, usable, modifiable**

This ensures:

- Structural integrity  
- Prevention of unauthorized implementations  
- Freedom for developers to use the agent runtime  

---

# 5. Author & Copyright
WLM-Agent  
Author: **Wujie Gu (Gavin)**  
Location: Melbourne, Australia  
Date: **10 February 2026**
