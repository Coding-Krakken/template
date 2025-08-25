# Resource Plan

- QA engineers

- Quarterly recalibration sessions
- Node.js (https://nodejs.org/) and pnpm (https://pnpm.io/) must be installed for development and builds
 - Required test packages: @testing-library/react-native, @types/jest
- Required npm packages: react, react-native, react/jsx-runtime, @types/react, @types/react-native
- Monaco Editor
- code-server
- React Native
- CI/CD tooling
- Node.js (https://nodejs.org/) and pnpm (https://pnpm.io/) must be installed for development and builds

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
