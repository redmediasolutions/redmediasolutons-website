# Red Media Solutions — Astro Website

Premium IT agency website built with **Astro** + **Tailwind CSS**. Pure Astro, no React, no heavy JS frameworks.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Project Structure

```
red-media-solutions/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Navigation.astro     — Fixed nav with mobile menu
│   │   ├── Hero.astro           — Hero with canvas particles
│   │   ├── Services.astro       — 6-service grid
│   │   ├── Products.astro       — Real products bento grid
│   │   ├── Work.astro           — Projects with HTML mockups
│   │   ├── Process.astro        — 4-step process section
│   │   ├── TechStack.astro      — Tech marquee + category cards
│   │   ├── Contact.astro        — Contact form + info
│   │   └── Footer.astro         — Footer with scroll-to-top
│   ├── layouts/
│   │   └── Layout.astro         — Base HTML + cursor + scroll reveal
│   ├── pages/
│   │   └── index.astro          — Main page
│   └── styles/
│       └── global.css           — Global styles, fonts, animations
├── astro.config.mjs
├── tailwind.config.mjs
├── tsconfig.json
└── package.json
```

## 🎨 Design System

- **Font**: Syne (display) + DM Sans (body)
- **Brand color**: `#e5173f`
- **Background**: `#0a0a0a`
- **Animations**: CSS-only scroll reveal, canvas particles, marquee

## 📞 Contact Details

- **Phone**: +91 95915 91783
- **Email**: redmediasolutins8@gmail.com
- **Location**: Bengaluru, Karnataka, India

## 🔧 Customisation

To update contact form submission, wire up the form in `src/components/Contact.astro` to your preferred service (Formspree, Netlify Forms, custom API).

## 🌐 Deploy

Works on **Vercel**, **Netlify**, **Cloudflare Pages** or any static host:

```bash
npm run build
# Upload the `dist/` folder
```
