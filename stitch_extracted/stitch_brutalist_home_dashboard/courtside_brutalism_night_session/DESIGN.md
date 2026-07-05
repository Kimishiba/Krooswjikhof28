---
name: 'Courtside Brutalism: Night Session'
colors:
  surface: '#0e131d'
  surface-dim: '#0e131d'
  surface-bright: '#343944'
  surface-container-lowest: '#090e17'
  surface-container-low: '#171c25'
  surface-container: '#1b2029'
  surface-container-high: '#252a34'
  surface-container-highest: '#30353f'
  on-surface: '#dee2f0'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#dee2f0'
  inverse-on-surface: '#2b303b'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#ffb4a7'
  on-secondary: '#680300'
  secondary-container: '#960801'
  on-secondary-container: '#ff9f8f'
  tertiary: '#abd600'
  on-tertiary: '#283500'
  tertiary-container: '#0a1000'
  on-tertiary-container: '#698500'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a7'
  on-secondary-fixed: '#400100'
  on-secondary-fixed-variant: '#920700'
  tertiary-fixed: '#c3f400'
  tertiary-fixed-dim: '#abd600'
  on-tertiary-fixed: '#161e00'
  on-tertiary-fixed-variant: '#3c4d00'
  background: '#0e131d'
  on-background: '#dee2f0'
  surface-variant: '#30353f'
typography:
  headline-xl:
    fontFamily: Anton
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Anton
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.1'
  headline-lg-mobile:
    fontFamily: Anton
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.1'
  body-lg:
    fontFamily: Archivo Narrow
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Archivo Narrow
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.0'
spacing:
  base: 4px
  gutter: 24px
  margin: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is a high-impact, industrial interpretation of sports aesthetics, specifically tailored for a dark, high-performance environment. It merges the raw, unrefined energy of **Brutalism** with the technical precision of a command-line interface. 

The target audience consists of data-focused athletes and enthusiasts who value clarity, speed, and a non-traditional "night session" atmosphere. The emotional response is one of intense focus, authoritative reliability, and kinetic energy. Visuals are defined by heavy strokes, solid blocks of color, and a total absence of gradients or soft transitions, favoring a "raw materials" approach to digital interface construction.

## Colors

The palette is built on **Deep Baseline Navy** (#0A0E1A) for the primary environment, ensuring high contrast for the foreground elements.

- **Primary (Deep Baseline Navy):** The foundational void. Used for global backgrounds.
- **Surface (Charcoal Navy):** Tonal variations (#161B26, #242933) used to define containers and interactive zones.
- **Accent 1 (Terracotta Red):** Derived from clay courts. Used for high-priority actions, alerts, and destructive states.
- **Accent 2 (Electric Optic Yellow):** Inspired by high-visibility tennis balls. Used for success states, active indicators, and critical data points.
- **Borders:** A consistent, high-visibility grey (#3D4455 or pure White for maximum impact) to define the brutalist structure.

## Typography

This design system utilizes a high-density typographic scale to mirror technical manuals and stadium signage.

- **Headlines (Anton):** Massive, condensed, and impactful. Always uppercase. These function more as architectural elements than simple text.
- **Body (Archivo Narrow):** Chosen for its high information density. It maintains legibility while feeling compact and "industrial."
- **Technical/Labels (JetBrains Mono):** Used for metadata, status labels, and data visualizations. The monospaced nature reinforces the "technical terminal" feel.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy with a rigid 12-column structure on desktop. 

- **Hard Gutters:** Gutters are clearly defined, often visually reinforced by vertical 1px divider lines in subtle navy (#1F2430).
- **Rhythm:** A 4px baseline grid governs all spacing.
- **Padding:** Internal container padding is generous (24px+) to offset the heavy, suffocating nature of thick borders.
- **Mobile:** Elements reflow to a single column, but maintain the 24px side margins to preserve the "framed" aesthetic.

## Elevation & Depth

True to the **Brutalism** movement, depth is not achieved through shadows that mimic light sources. Instead, this design system uses **Hard-Drop Shadows**.

- **Shadow Character:** Solid, 100% opacity offsets. A shadow is a solid block of color (usually Black or Deep Navy) offset by 4px or 8px.
- **Z-Axis:** Higher elevation is communicated by increasing the offset of the hard shadow, making the element look like it is physically pushed away from the background.
- **Interaction:** On hover, buttons should "press" into their shadow (offset shifts from 4px to 0px).
- **Outlines:** Every surface must have a minimum 2px solid border to separate it from the Deep Baseline Navy background.

## Shapes

The design system is strictly **Sharp (0)**. There are no rounded corners. 

- **Geometry:** 90-degree angles emphasize the industrial, uncompromising nature of the brand.
- **Cuts:** Use 45-degree chamfered corners occasionally for "Action" buttons to suggest a technical, military, or high-performance equipment feel.
- **Dividers:** Thick, solid lines are used to separate sections rather than whitespace alone.

## Components

- **Buttons:** Rectangular with 3px solid borders. Primary buttons use Terracotta Red background with Black text. Secondary buttons are transparent with Electric Optic Yellow borders and text.
- **Cards:** Use Charcoal Navy (#161B26) background. Must feature a 4px solid black hard-drop shadow.
- **Inputs:** High-contrast boxes with JetBrains Mono text. Active state triggers an Electric Optic Yellow border.
- **Chips/Status:** Small, sharp-edged blocks. Use Electric Optic Yellow for "Live" or "Active" and Terracotta Red for "Closed" or "Error."
- **Lists:** Separated by 2px horizontal rules. Use monospaced font for list indices (e.g., 01, 02, 03).
- **Progress Bars:** Blocky and segmented. Do not use smooth fills; use discrete blocks to show progress, reminiscent of vintage LED displays.