---
name: beautiful-web-design
description: Design, build, review, and improve polished,
  responsive websites and web application interfaces.
  Use for frontend UI creation, visual redesign, React
  components, mobile-first layouts, design systems,
  landing pages, dashboards, and web app interfaces.
---

# Beautiful Web Design

Create polished, usable, and responsive web interfaces
with consistent visual quality and maintainable code.

## 1. Understand the Task

Before implementation:

1. Identify the product and target audience.
2. Identify the primary user journey.
3. Determine the required pages and interactions.
4. Inspect existing code and design conventions.
5. Confirm constraints that materially affect the result.

For open-ended tasks, make reasonable design decisions
and explain important assumptions.

## 2. Define the Design Direction

Select a visual direction suitable for the product.

Establish:

- Color palette
- Typography scale
- Spacing system
- Border radius and elevation
- Component states
- Responsive breakpoints

Do not force one aesthetic across unrelated products.

For detailed guidance, read:
references/design-guidelines.md

## 3. Design Mobile First

Start with the smallest practical viewport.

Ensure:

- Readable typography
- Touch-friendly controls
- Clear navigation
- No horizontal overflow
- Appropriate content priority

Extend the layout to tablet and desktop screens.

## 4. Build Reusable Components

Prefer reusable and composable components.

When using React:

- Separate presentation from business logic.
- Use typed props when TypeScript is available.
- Keep state near its consumers.
- Avoid unnecessary re-renders.
- Preserve established project conventions.

Use existing dependencies where practical.

Do not introduce new frameworks without a clear need.

## 5. Implement Real Interactions

Every visible interactive control should have
a meaningful and predictable behavior.

Provide appropriate:

- Loading states
- Empty states
- Error states
- Success feedback
- Keyboard interactions
- Accessible labels

Never present mock functionality as a working
backend integration.

## 6. Preserve Existing Functionality

When redesigning an existing interface:

1. Inspect current components and user flows.
2. Identify functionality that must be preserved.
3. Modify only what the request requires.
4. Avoid unnecessary architecture changes.
5. Verify important interactions after modification.

## 7. Review Visual Quality

Check the interface for:

- Visual hierarchy
- Alignment and spacing
- Typography consistency
- Color contrast
- Image quality
- Responsive behavior
- Interaction feedback
- Unnecessary decoration

Use available browser or preview tools when possible.

Do not claim visual verification without
actually inspecting the rendered interface.

## 8. Validate and Deliver

Run relevant project checks where available.

Verify:

- Main user journey
- Essential controls
- Mobile layout
- Desktop layout
- Empty and error states
- No obvious layout regression

Report:

1. What was implemented
2. Important design decisions
3. What was verified
4. Known limitations
5. Recommended next improvements
