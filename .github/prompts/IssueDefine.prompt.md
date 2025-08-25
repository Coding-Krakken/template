# Copilot Issue Definition Prompt

## Dual Root Guidance
This repository has two project roots:
- The **application root** (current working directory) is for the main product code and development.
- The **template root** (`template/`) contains the Universal Hybrid Process Template and all auxiliary files/artifacts for process enforcement, traceability, and evidence.

Copilot must always distinguish which root a file or artifact belongs to. Application code, features, and product development are in the application root. Process, workflow, gates, artifacts, and compliance files are in the template root. All instructions, prompts, and automation should explicitly reference the correct root for each file or artifact.

## Purpose
This prompt guides Copilot to help the user define a specific issue in detail, then automatically creates the issue file in `.github/issues/` using the provided information. The workflow and logic should mirror `Issue.prompt.md`, but with a focus on issue definition and creation.

---

## Instructions for Copilot
1. **Engage the user to clarify and define the issue:**
   - Ask targeted questions to gather all necessary details (title, description, context, expected outcome, severity, related files, etc.).
   - Confirm the scope and specifics before proceeding.
2. **Generate the issue file:**
   - Use the collected details to create a new markdown file in `.github/issues/`.
   - Name the file according to the next available issue number (e.g., `6.md`).
   - Follow the formatting and logic of `Issue.prompt.md` for consistency.
3. **Output summary:**
   - Summarize the defined issue and confirm creation.
   - Provide next steps or follow-up actions if relevant.

---

## Example Workflow
1. Copilot: "Please describe the issue you want to define. Include as much detail as possible."
2. User: [Provides details]
3. Copilot: "Is this issue related to any specific files or features? What is the expected outcome?"
4. User: [Provides more info]
5. Copilot: "Thank you. I will now create the issue in `.github/issues/6.md`."
6. Copilot: [Creates file, confirms, and summarizes]

---

## Logic Reference
- Use the same logic and formatting as `Issue.prompt.md` for issue creation and file structure.
- Ensure atomic, standards-aligned steps.
- Record decisions and outputs as per repo conventions.
