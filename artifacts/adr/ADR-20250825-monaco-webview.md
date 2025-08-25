---
title: "Monaco Editor Integration via WebView in Mobile Client"
date: 2025-08-25
author: "Open Code Remote Team"
status: "Accepted"
context:
  - Product vision: Remote-first mobile VS Code client
  - Architecture: Mobile app uses React Native, Monaco editor in WebView for code editing
  - Requirements: Mobile ergonomics, performance, security, extensibility
  - Alternatives: Native editor, other web-based editors
---

# Decision

We will integrate the Monaco code editor into the mobile client using a WebView wrapper. This enables full VS Code editing capabilities, leverages existing Monaco APIs, and supports mobile-specific UX enhancements (selection handles, find/replace, add-cursor button).

# Rationale
- Aligns with VS Code/Code OSS standards and user expectations
- Enables feature parity with desktop code-server
- Supports mobile ergonomics and future extensibility
- Reduces implementation risk by reusing proven editor technology

# Consequences
- Requires bridge for file operations, key events, and mobile gestures
- WebView performance must be optimized for mobile devices
- Security and privacy must be enforced at the WebView boundary

# Traceability
- Linked to product vision in `docs/vision.md`
- Supported by architecture in `docs/architecture/README.md`
- Enables features in `apps/mobile/src/components/EditorWebView.tsx`
- Test coverage to be tracked in CI and traceability matrix
