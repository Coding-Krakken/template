
- Secure transport modules (SSH, HTTP, WebSocket) integrated
- Team: Mobile engineers, backend engineers, security/compliance, QA
 - Required test packages: @testing-library/react-native, @types/jest, and related type declarations must be installed for mobile app testing
- Capacity: 2-week sprints, quarterly recalibration

## Q3 2025
- [ ] Automerge PRs that pass all gates
- [ ] Add cost/performance budgets enforcement
- [ ] Enable progressive delivery guardrails (flags, canaries)
- [ ] Expand recalibration automation (metrics-driven)
- [ ] Mobile Monaco Editor: finalize integration and test coverage
- [ ] Document traceability matrix for all critical features

- Next priorities:
	- Automerge PRs that pass all gates
	- Add cost/performance budgets enforcement
	- Enable progressive delivery guardrails (flags, canaries)
	- Expand recalibration automation (metrics-driven)
	- Mobile Monaco Editor: finalize integration and test coverage ([ADR-20250825-monaco-webview.md](../artifacts/adr/ADR-20250825-monaco-webview.md))
	- Document traceability matrix for all critical features ([traceability_matrix.md](traceability_matrix.md))
	- Implement Explorer, Editor, and Terminal features:
		- Integrate file tree logic in Explorer (link to fileops module)
		- Integrate Monaco Editor in Editor (link to EditorWebView)
		- Integrate terminal logic in Terminal (link to TerminalWebView)
		- Ensure all components meet requirements and traceability matrix
		- Achieve full test coverage for all components
		- Ensure all new features meet compliance, privacy, and performance gates

---

*Update this file as new features and priorities are added. Link to ADRs, RFCs, gate evidence, and the [traceability matrix](traceability_matrix.md) as needed.*

## Onboarding Instructions (Environment Setup)

1. Install [Node.js](https://nodejs.org/) (includes npm).
2. Install [pnpm](https://pnpm.io/) globally: `npm install -g pnpm`
3. In the repo root, run: `pnpm install`
4. In `apps/mobile`, run: `pnpm install`
5. Install required packages for mobile app:
   - `pnpm add react react-native react/jsx-runtime`
   - `pnpm add -D @types/react @types/react-native @types/jest @testing-library/react-native`
6. Verify that all errors in components and tests are resolved.
7. Proceed with development and commit changes once all problems are fixed.
