---
name: Forest Punk Kinetic
colors:
  surface: '#f9f9f6'
  surface-dim: '#dadad7'
  surface-bright: '#f9f9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f1'
  surface-container: '#eeeeeb'
  surface-container-high: '#e8e8e5'
  surface-container-highest: '#e2e3e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#414940'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f1f1ee'
  outline: '#717970'
  outline-variant: '#c0c9be'
  surface-tint: '#326a3f'
  primary: '#00280e'
  on-primary: '#ffffff'
  primary-container: '#00401a'
  on-primary-container: '#73ad7b'
  inverse-primary: '#99d5a0'
  secondary: '#a33800'
  on-secondary: '#ffffff'
  secondary-container: '#cd4800'
  on-secondary-container: '#fffbff'
  tertiary: '#430c1c'
  on-tertiary: '#ffffff'
  tertiary-container: '#5e2231'
  on-tertiary-container: '#db8898'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b4f1bb'
  primary-fixed-dim: '#99d5a0'
  on-primary-fixed: '#00210a'
  on-primary-fixed-variant: '#175129'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#802a00'
  tertiary-fixed: '#ffd9de'
  tertiary-fixed-dim: '#ffb2bf'
  on-tertiary-fixed: '#3b0617'
  on-tertiary-fixed-variant: '#723241'
  background: '#f9f9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e2e3e0'
typography:
  display-2xl:
    fontFamily: Archivo Narrow
    fontSize: 120px
    fontWeight: '800'
    lineHeight: 100px
    letterSpacing: -0.04em
  display-lg:
    fontFamily: Archivo Narrow
    fontSize: 80px
    fontWeight: '800'
    lineHeight: 72px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Archivo Narrow
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Archivo Narrow
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Archivo Narrow
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: '0'
  body-md:
    fontFamily: Archivo Narrow
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  label-mono:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
spacing:
  base_unit: 4px
  gutter: 1px
  margin-page: 32px
  container-max: 1440px
---

## Brand & Style
This design system is a high-octane evolution of Swiss Punk, merging the raw structural integrity of the International Typographic Style with a kinetic, contemporary Brutalism. The brand personality is unapologetic, authoritative, and high-energy. It targets a sophisticated audience that values radical clarity over decorative fluff.

The aesthetic utilizes "Forest Punk"—a palette shift that replaces clinical blues with a deep, organic tension. It relies on massive typographic hierarchies, heavy strokes, and an uncompromising grid. The emotional response is one of urgency and precision; the UI should feel like a physical broadsheet poster that has been electrified.

## Colors
The palette is built on high-contrast tension. 
- **Primary:** A deep, near-black Forest Green (#00401A) serves as the primary structural anchor, used for heavy borders, primary buttons, and dominant headers.
- **Secondary:** A vibrant, saturated Kinetic Orange (#FF5C00) is used sparingly for interaction cues, critical alerts, and focal points.
- **Surface:** A warm, off-white neutral (#F4F4F1) prevents the design from feeling sterile, providing a "paper" quality to the background.
- **Interaction:** All interactive elements utilize the primary green as the default state, shifting to orange only on high-priority actions or active states.

## Typography
Typography is the primary visual engine of this design system. We use **Archivo Narrow** for its compact, aggressive verticality, allowing for massive "Display" sizes that command the layout.
- **Oversized Headers:** Display sizes must be set with tight leading (often less than 100% of font size) to create a dense, block-like visual effect.
- **Monospaced Utility:** **Space Mono** is used for labels, metadata, and captions to reinforce the technical, brutalist undertone.
- **Alignment:** Forceful left-alignment is the default. Avoid center alignment for large blocks of text.

## Layout & Spacing
The layout follows a strict **12-column Swiss Grid**. 
- **The "Heavy Line" Rule:** Columns are separated by 1px or 2px solid strokes in the primary forest green rather than invisible gutters.
- **In-set Padding:** Content never touches these borders; use a consistent 16px or 24px internal padding within grid cells.
- **Responsive Behavior:** On mobile, the 12 columns collapse to 2 or 4, but the 1px divider lines remain a constant visual anchor. Vertical rhythm is dictated by a 4px baseline grid.

## Elevation & Depth
This design system rejects shadows and blurs entirely. Depth is achieved through **hard layering and heavy borders**.
- **Flat Stacking:** Elements do not "float." They are either flush with the surface or "raised" using a secondary solid border to create a 2D offset effect.
- **Bold Outlines:** Every container, card, and input field must have a minimum 2px solid border in the primary forest green. 
- **High-Contrast Overlays:** Modals do not use background blurs; they use a solid 90% opacity Forest Green overlay to completely isolate the user's focus.

## Shapes
The shape language is strictly **Sharp (0)**. There are no rounded corners in this design system. Every button, input field, card, and image container must have 90-degree angles. This geometric rigidity is essential to maintaining the "Punk" and "Brutalist" aesthetic.

## Components
- **Buttons:** Large, rectangular blocks with 2px Forest Green borders. Primary buttons use a solid Forest Green fill with white text. Secondary/Action buttons use Kinetic Orange fill. On hover, apply a 4px hard-offset "shadow" using the primary green.
- **Inputs:** Simple boxes with 2px borders. Labels use `label-mono` and sit directly above the border or are "notched" into the top-left of the border stroke.
- **Cards:** Defined by their grid borders. If a card needs to stand out, use a Forest Green background with white text (`inverted` state).
- **Lists:** Separated by horizontal 1px lines. Every list item should have a hover state that fills the entire row with a light grey or Kinetic Orange for high-priority items.
- **Chips/Tags:** Sharp-edged boxes using `label-mono`. Use high-contrast fills (Forest Green for categories, Kinetic Orange for status).
- **Navigation:** A persistent sidebar or top bar with heavy-weight borders, using archival-style numbering (01, 02, 03) in Space Mono alongside nav items.