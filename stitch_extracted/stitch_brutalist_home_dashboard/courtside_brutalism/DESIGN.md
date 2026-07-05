---
name: Courtside Brutalism
colors:
  surface: '#f4ffc9'
  surface-dim: '#cee38d'
  surface-bright: '#f4ffc9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e8fda4'
  surface-container: '#e2f79f'
  surface-container-high: '#dcf19a'
  surface-container-highest: '#d7ec95'
  on-surface: '#161e00'
  on-surface-variant: '#55433e'
  inverse-surface: '#293500'
  inverse-on-surface: '#e5faa2'
  outline: '#88726d'
  outline-variant: '#dbc1bb'
  surface-tint: '#984631'
  primary: '#94422e'
  on-primary: '#ffffff'
  primary-container: '#b35a44'
  on-primary-container: '#fffaf9'
  inverse-primary: '#ffb4a2'
  secondary: '#545e76'
  on-secondary: '#ffffff'
  secondary-container: '#d7e2ff'
  on-secondary-container: '#5a647c'
  tertiary: '#4d6300'
  on-tertiary: '#ffffff'
  tertiary-container: '#637d00'
  on-tertiary-container: '#f8ffd9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad2'
  primary-fixed-dim: '#ffb4a2'
  on-primary-fixed: '#3c0700'
  on-primary-fixed-variant: '#7a2f1c'
  secondary-fixed: '#d7e2ff'
  secondary-fixed-dim: '#bbc6e2'
  on-secondary-fixed: '#101b30'
  on-secondary-fixed-variant: '#3c475d'
  tertiary-fixed: '#c3f400'
  tertiary-fixed-dim: '#abd600'
  on-tertiary-fixed: '#161e00'
  on-tertiary-fixed-variant: '#3c4d00'
  background: '#f4ffc9'
  on-background: '#161e00'
  surface-variant: '#d7ec95'
typography:
  headline-xl:
    fontFamily: Archivo Narrow
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Archivo Narrow
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Archivo Narrow
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
  body-md:
    fontFamily: Archivo Narrow
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  detail-serif:
    fontFamily: Libre Caslon Text
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Archivo Narrow
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  border-weight: 4px
  gutter: 24px
  margin-edge: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 48px
---

## Brand & Style
This design system merges the raw, structural integrity of industrial brutalism with the vibrant, social energy of a Mediterranean tennis club. The aesthetic is "Forest Punk"—characterized by thick strokes, heavy-handed borders, and an unapologetic use of screen real estate. It targets a bold, design-literate audience that values functional clarity served with high-impact personality.

The UI evokes a sense of "technical heritage": the reliability of a clay court mixed with the sharp, modern edge of professional sports gear. By utilizing an asymmetric grid and "hard" depth effects, the design system avoids the softness of modern SaaS trends in favor of a grounded, authoritative, and physically present digital experience.

## Colors
The palette is a high-contrast dialogue between earthy Mediterranean tones and synthetic sports accents. 

- **Surface (#F8F9FA):** A bleached linen white that acts as the canvas for heavy linework.
- **Primary (#B35A44):** Terracotta Red, used for key actions and structural highlights, reminiscent of clay courts.
- **Secondary (#1B263B):** Deep Baseline Navy, used for all borders, shadows, and primary text to ensure maximum legibility and "ink" weight.
- **Accent (#CCFF00):** Electric Optic Yellow, reserved for high-priority call-to-outs, badges, and "active" states.
- **Neutral (#708238):** Spanish Olive, utilized for secondary UI elements, success states, or grounding background sections.

## Typography
Typography is treated as a structural element. **Archivo Narrow** provides a compressed, industrial strength for headlines and functional text, allowing for massive scale without sacrificing horizontal space. 

To provide a "Tapas" editorial flair, **Libre Caslon Text** is used sparingly for secondary details, quotes, or descriptions. This high-contrast serif breaks the rigidity of the brutalist layout with a touch of classic sophistication. Use "headline-xl" for hero sections, ensuring it overlaps or sits tight against borders to emphasize the crowded, energetic layout.

## Layout & Spacing
The layout ignores standard symmetry. Use a **12-column asymmetric fluid grid** where content blocks are intentionally offset. For example, a left-hand column might span 7 columns while the right spans 5, but with varying top-margins to create a "staircase" effect.

- **Borders:** A universal 4px border (Deep Baseline Navy) must be applied to all primary containers.
- **Gutters:** Maintain a strict 24px gap between blocks. 
- **Padding:** Use generous internal padding (32px+) within containers to balance the "heavy" borders.
- **Mobile:** Collapse the asymmetric offsets into a single column but maintain the 4px borders and hard shadows to preserve the brand's weight.

## Elevation & Depth
This system rejects blurs and gradients. Depth is achieved exclusively through **Hard Shadows** (Neobrutalism style). 

All interactive containers (Cards, Buttons) should feature a 4px or 8px offset shadow in **Deep Baseline Navy (#1B263B)**. The shadow has 100% opacity and 0px blur radius. When an element is "pressed," the shadow should disappear (0px offset), simulating the element being physically pushed into the page. Overlapping layers should use the 4px border to define boundaries rather than atmospheric shadows.

## Shapes
The shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields must feature 90-degree corners. This reinforces the industrial, "Forest Punk" architectural feel and ensures the 4px borders connect seamlessly at the vertices. Avoid circles even for avatars; use squares or octagons with 4px borders instead.

## Components
- **Buttons:** Rectangular with 4px Navy borders and a 4px hard shadow. Default state is Terracotta Red (#B35A44) with white text. Hover state shifts the background to Electric Optic Yellow (#CCFF00) with Navy text.
- **Cards:** Use the Surface color (#F8F9FA) for the background, wrapped in a 4px Navy border. Headlines within cards should be flush against the top-left margin.
- **Inputs:** White background, 4px Navy border. On focus, the border remains, but the background shifts to a very light tint of Optic Yellow.
- **Chips/Badges:** Small rectangular boxes with 2px borders. Use Spanish Olive (#708238) for informational tags.
- **Lists:** Separate list items with a 4px horizontal Navy rule. Do not use rounded dividers.
- **Special Component - "The Scoreboard":** A distinctive data-display component using large Archivo Narrow numbers, heavy borders, and an Electric Optic Yellow background to highlight current status or key metrics.