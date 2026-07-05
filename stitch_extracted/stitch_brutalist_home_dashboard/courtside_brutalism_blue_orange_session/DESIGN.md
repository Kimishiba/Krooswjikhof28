---
name: 'Courtside Brutalism: Blue & Orange Session'
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c5d9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e90a2'
  outline-variant: '#434656'
  surface-tint: '#b8c3ff'
  primary: '#b8c3ff'
  on-primary: '#002387'
  primary-container: '#2d5bff'
  on-primary-container: '#efefff'
  inverse-primary: '#104af0'
  secondary: '#ffb59a'
  on-secondary: '#5a1b00'
  secondary-container: '#ff5e07'
  on-secondary-container: '#531900'
  tertiary: '#00dbe9'
  on-tertiary: '#00363a'
  tertiary-container: '#007981'
  on-tertiary-container: '#c4faff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c3ff'
  on-primary-fixed: '#001355'
  on-primary-fixed-variant: '#0035bd'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#802a00'
  tertiary-fixed: '#7df4ff'
  tertiary-fixed-dim: '#00dbe9'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Anton
    fontSize: 80px
    fontWeight: '400'
    lineHeight: 80px
  headline-lg:
    fontFamily: Anton
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: Anton
    fontSize: 36px
    fontWeight: '400'
    lineHeight: 36px
  headline-md:
    fontFamily: Anton
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 28px
  body-lg:
    fontFamily: Archivo Narrow
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Archivo Narrow
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
This design system is a high-energy, performance-driven evolution of digital brutalism. It targets a bold, athletic audience that values raw intensity and unapologetic clarity. The emotional response is one of adrenaline, focus, and industrial strength.

The style leverages **Neo-Brutalism**:
- **Raw Typography:** Massive, condensed headings that command the screen.
- **Structural Integrity:** Heavy, visible strokes (2px+) and hard, non-diffused shadows.
- **High-Contrast Dark Mode:** A deep charcoal foundation that makes vibrant accents vibrate against the background.
- **Grid-Dominance:** Layouts are intentional, rigid, and follow a strict structural rhythm, mimicking the lines of a night-lit sports court.

## Colors
The palette is built on a "Night Session" foundation of deep blacks and charcoals, punctuated by high-luminance technical colors.

- **Primary (Courtside Blue):** A deep, saturated blue (#2D5BFF) used for primary interactive states, key brand moments, and structural accents.
- **Secondary (Ignite Orange):** A bright, high-energy orange (#FF5C00) reserved for status indicators, warnings, and high-visibility alerts that require immediate attention.
- **Tertiary (Oxygen Cyan):** A sharp, electric cyan (#00F0FF) used for data visualization and secondary interactive highlights.
- **Surface:** The primary background is #0F0F0F, with containers utilizing #1A1A1A to maintain a brutalist, low-gradient environment.
- **Stroke/Border:** All borders use #FFFFFF at 100% opacity for high-impact definition or #333333 for subtle grid-work.

## Typography
Typography is treated as a structural element. 
- **Display:** Anton provides the impactful, condensed verticality required for the brutalist aesthetic. Use it for all major headings and impact statements.
- **Interface:** Archivo Narrow keeps body text efficient and legible in high-density data environments.
- **Data/Technical:** JetBrains Mono is used for labels, timestamps, and secondary metadata to reinforce the technical, industrial nature of the system.
- **Treatment:** Headings should predominantly be uppercase. Avoid thin weights; maintain a "heavy" visual density across all levels.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid Grid**:
- **Structure:** 12-column grid for desktop with 24px gutters. Use heavy 2px vertical rules to separate columns in complex dashboard views.
- **Rhythm:** An 8px base unit drives all padding and margins, but 4px is allowed for tight component-level spacing.
- **Margins:** Large outer margins (40px+) create a "frame" effect, making the central content feel like a broadcast feed or a scoreboard.
- **Alignment:** Strict top-left alignment for all text. Avoid centered blocks unless they are massive display headlines.

## Elevation & Depth
Depth is created through **Hard Offsets** rather than light-based shadows:
- **The "Brutalist Shadow":** Elements do not float; they are extruded. Use a 4px or 8px offset shadow with 100% opacity in Primary Blue or Solid Black.
- **Layering:** Hierarchy is established by stack order and border thickness. Elements higher in the hierarchy have thicker borders (3px) compared to base elements (1px or 2px).
- **Z-Index Visuals:** Overlapping elements should have a clear high-contrast stroke to separate them from the background. No blurs or gradients are permitted.

## Shapes
The shape language is strictly **Sharp (0)**. 
- All buttons, cards, inputs, and containers must have 90-degree corners. 
- Use diagonal "clipped" corners (45-degree cuts) only for special decorative elements or primary action buttons to evoke a futuristic, technical feel.
- Icons should be stroke-based with square caps and joins to match the typography.

## Components
- **Buttons:** Primary buttons use a solid Blue background with Black text and a Hard Black shadow offset. Secondary buttons are transparent with a 2px White border.
- **Inputs:** High-contrast White borders on Black backgrounds. The active state uses a 4px Blue border.
- **Status Indicators:** Use Ignite Orange (#FF5C00) for "Live" or "Alert" states. Use a solid square or a thick underline rather than a circular dot.
- **Cards:** Cards use a #1A1A1A background with a 1px border. Important cards (e.g., featured matches or stats) receive a 4px left-hand border in Primary Blue.
- **Selection Controls:** Checkboxes and Radio buttons are strictly square. The "selected" state fills the square with Blue and a White "X" or inner square.
- **Data Tables:** Use heavy horizontal separators (2px) and JetBrains Mono for all numeric values to ensure maximum readability and a "technical readout" aesthetic.