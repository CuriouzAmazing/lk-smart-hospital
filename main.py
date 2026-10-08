import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components

with open("C:/Users/SESA731787/OneDrive - Schneider Electric/BITS/Dissertation/tmz-support-bot/lk-smart-hospital/assets/lklogopng2.png", "rb") as f:
    logo = base64.b64encode(f.read()).decode()

#------------------- TITLEBAR CONTENT ----------------------
im = Image.open("C:/Users/SESA731787/OneDrive - Schneider Electric/BITS/Dissertation/tmz-support-bot/lk-smart-hospital/assets/lklogo.ico")

st.set_page_config(
page_title="Lauritz Knudsen Smart Hospital",
page_icon=im,
layout="wide",
initial_sidebar_state="collapsed"
)

#------------------- TITLE ----------------------------------
#st.title("Lauritz Knudsen Smart Hospital")
#   st.subheader("Brewed by Lauritz Knudsen Electrical & Automation")

#-------------------HEADER, TAGLINE & LOGO-----------------------------------
left_space, right_col = st.columns([8, 1])
with right_col:
    st.write()
    #st.image("C:/Users/SESA731787/OneDrive - Schneider Electric/BITS/Dissertation/tmz-support-bot/lk-smart-hospital/assets/lklogopng.png", width = 150)
with left_space:
    st.title("Smart Multispeciality Hospital by Lauritz Knudsen")
    st.subheader("Transforming hospital operations through connected infrastructure, real-time visibility and intelligent energy management to enhance patient care, reliability and sustainability")

#------------------ APP BAR - TOP NAV BAR----------------------------------------------

st.markdown(
    """
    <style>
    /* Hide Streamlit's default header and reduce top container padding */
    [data-testid="stHeader"] {
        display: none;
    }
    [data-testid="stMainBlockContainer"] {
        padding-top: 1rem;
    }

    /* Navbar Container Styles */
    .top-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(90deg,#0f172a,#1e293b);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 50px 50px;
        z-index: 99999;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Logo/Brand Style */
    .logo-container {
    display: flex;
    align-items: center;
    }
    .logo-container img {
        height: auto; /* Force image height to fit perfectly in the navbar */
        width: 150px;  /* Preserve the logo aspect ratio */
        object-fit: contain;
    }
    
    /* Navigation Links Container */
    .navbar-links {
        display: flex;
        gap: 30px;
    }
    
    /* Navigation Links Styles */
    .navbar-links a {
        color: #FFFFFF;
        text-decoration: none;
        font-size: 20px;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .navbar-links a:hover {
        color: #005B8C;
    }

    .block-container {
    padding-top: 150px;             /* Space inside the container */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Render the Navbar HTML


st.markdown(
    f"""
    <div class="top-navbar">
        <a href = "#overview" class="logo-container">
            <img src="data:image/png;base64,{logo}" alt="Logo">
        </a>
        <div class="navbar-links">
            <a href="#electricalandupsroom">Electrical & UPS Room</a>
            <a href="#icuandot">ICU & OT</a>
            <a href="#oxygenandgassystem">Oxygen & Gas System</a>
            <a href="#hvacsystem">HVAC System</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# From 2508
HTML = r'''
<!doctype html>
<html lang="en">
<head>
    <!-- Define UTF-8 encoding for symbols such as O₂ and icons. -->
    <meta charset="utf-8">

    <!-- Make the interface scale correctly on laptops, tablets, and phones. -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Set the title used inside the embedded page. -->
    <title>Smart Hospital Infrastructure Explorer</title>

    <style>
        /* Define reusable colors for the entire application. */
        :root {
            --background: #050d17;
            --surface: rgba(7, 23, 38, 0.94);
            --border: rgba(255, 255, 255, 0.12);
            --text: #f7fbff;
            --muted: #9bafc2;
            --cyan: #25d5f2;
            --green: #43e29f;
            --red: #ff657b;
            --amber: #ffbd59;
            --violet: #a78bfa;
            --blue: #5b8cff;
        }

        /* Use predictable element sizing throughout the interface. */
        * { box-sizing: border-box; }

        /* Fill the iframe and prevent duplicate browser scroll bars. */
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            overflow: hidden;
            color: var(--text);
            background: var(--background);
            font-family: Inter, "Segoe UI", Arial, sans-serif;
        }

        /* Create the full-screen application background. */
        .app {
            position: relative;
            width: 100vw;
            height: 100vh;
            min-height: 760px;
            overflow: hidden;
            background: radial-gradient(circle at 50% 32%, #173d5c 0%, #081725 46%, #040a12 100%);
        }

        /* Position the title and system filter controls above the hospital. */
        .header {
            position: absolute;
            z-index: 30;
            top: 18px;
            left: 22px;
            right: 22px;
            display: flex;
            justify-content: space-between;
            gap: 16px;
            pointer-events: none;
        }
/* Apply a shared glass-panel appearance. */
        .glass {
            pointer-events: auto;
            border: 1px solid var(--border);
            background: rgba(6, 21, 34, 0.86);
            backdrop-filter: blur(17px);
            box-shadow: 0 16px 48px rgba(0, 0, 0, 0.42);
        }

        /* Style the application title card. */
        .brand { padding: 14px 17px; border-radius: 18px; }

        /* Style the main heading. */
        .brand h1 { margin: 0; font-size: clamp(18px, 2vw, 24px); }

        /* Style the short usage instruction. */
        .brand p { margin: 5px 0 0; color: var(--muted); font-size: 12px; }

        /* Arrange the system filter buttons in one row. */
        .filters { display: flex; gap: 7px; padding: 7px; border-radius: 16px; }

        /* Style each system filter button. */
        .filters button {
            padding: 9px 11px;
            border: 1px solid transparent;
            border-radius: 10px;
            color: #aebed0;
            background: transparent;
            font-weight: 700;
            cursor: pointer;
        }

        /* Indicate the active or hovered system filter. */
        .filters button:hover, .filters button.active {
            color: white;
            border-color: rgba(37, 213, 242, 0.28);
            background: rgba(37, 213, 242, 0.10);
        }

        /* Create the main visualization card. */
        .stage {
            position: absolute;
            inset: 92px 18px 18px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 28px;
            background: linear-gradient(180deg, rgba(11, 43, 67, 0.86), rgba(5, 14, 24, 0.92));
            box-shadow: inset 0 1px rgba(255, 255, 255, 0.04), 0 35px 100px rgba(0, 0, 0, 0.56);
        }

        /* Leave space on the right for floor controls. */
        .visual { position: absolute; inset: 0 285px 0 0; }

        /* Scale the vector hospital to the available space. */
        .visual svg { width: 100%; height: 100%; display: block; }

        /* Make all clinical and utility zones visibly interactive. */
        .zone { cursor: pointer; outline: none; }

        /* Animate zone surfaces when selected or hovered. */
        .zone .surface { transition: filter 0.22s ease, opacity 0.22s ease; }

        /* Brighten a zone when the pointer moves over it. */
        .zone:hover .surface, .zone.active .surface { filter: brightness(1.22); }

        /* Move a marker slightly upward when hovered. */
        .zone:hover .pin { transform: translateY(-5px); }

        /* Animate each clickable marker smoothly. */
        .pin { transition: transform 0.22s ease; filter: drop-shadow(0 8px 8px rgba(0, 0, 0, 0.55)); }

        /* Animate the utility routes to suggest direction of flow. */
        .flow {
            fill: none;
            stroke-linecap: round;
            stroke-dasharray: 8 10;
            animation: route-flow 1.6s linear infinite;
        }

        /* Move the dash pattern continuously along each route. */
        @keyframes route-flow { to { stroke-dashoffset: -36; } }

        /* Rotate the AHU fan symbols. */
        .fan {
            transform-box: fill-box;
            transform-origin: center;
            animation: fan-spin 5s linear infinite;
        }

        /* Complete one full fan rotation. */
        @keyframes fan-spin { to { transform: rotate(360deg); } }

        /* Dim floors that are not selected in floor-focus mode. */
        .floor.dim { opacity: 0.10; filter: saturate(0.2); }

        /* Animate floor focus changes rather than switching abruptly. */
        .floor { transition: opacity 0.3s ease, filter 0.3s ease; }

        /* Style labels drawn inside the SVG. */
        .floor-label { fill: #c7f5ff; font-size: 11px; font-weight: 900; letter-spacing: 1.3px; }

        /* Style labels used beside clickable markers. */
        .marker-label { fill: white; font-size: 12px; font-weight: 800; }

        /* Position the floor selector on the right of the stage. */
        .floor-panel { position: absolute; z-index: 15; right: 50px; top: 68px; width: 248px; padding: 20px; border-radius: 17px; }

        /* Style the floor selector heading. */
        .floor-panel h3 { margin: 0 0 9px; color: var(--muted); font-size: 9px; letter-spacing: 0.15em; }

        /* Arrange floor buttons in a compact grid. */
        .floor-buttons { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }

        /* Style floor selector buttons. */
        .floor-buttons button {
            padding: 8px 5px;
            border: 1px solid var(--border);
            border-radius: 9px;
            color: #afc0d1;
            background: rgba(255, 255, 255, 0.04);
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }

        /* Highlight the selected floor button. */
        .floor-buttons button.active { color: white; border-color: rgba(37, 213, 242, 0.4); background: rgba(37, 213, 242, 0.11); }
        .floor-buttons button:hover { color: white; border-color: var(--cyan); }

        /* Position the quick-access system buttons. */
        .quick-links { position: absolute; z-index: 15; right: 50px; top: 220px; width: 248px; padding: 13px; border-radius: 17px; }

        /* Style the quick-access title. */
        .quick-links h3 { margin: 0 0 9px; font-size: 13px; }

        /* Make each quick-access link a clear full-width target. */
        .quick-links button {
            width: 100%;
            margin-top: 6px;
            padding: 9px 10px;
            border: 1px solid var(--border);
            border-radius: 10px;
            color: #c5d2df;
            background: rgba(255, 255, 255, 0.035);
            text-align: left;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
        }

        /* Provide visual feedback on quick-access buttons. */
        .quick-links button:hover { color: white; border-color: var(--cyan); }

        /* Create the right-side detail drawer. */
        .drawer {
            position: absolute;
            z-index: 50;
            top: 98px;
            right: 20px;
            bottom: 20px;
            width: min(420px, calc(100vw - 28px));
            overflow: hidden;
            border: 1px solid var(--border);
            border-radius: 24px;
            background: var(--surface);
            backdrop-filter: blur(20px);
            box-shadow: 0 30px 100px rgba(0, 0, 0, 0.75);
            transform: translateX(calc(100% + 50px));
            transition: transform 0.38s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        /* Slide the drawer into view after a zone is selected. */
        .drawer.open { transform: translateX(0); }

        /* Arrange the system icon, title, and close button. */
        .drawer-header { display: flex; gap: 10px; align-items: flex-start; padding: 20px; border-bottom: 1px solid var(--border); }

        /* Style the system icon. */
        .system-icon { width: 50px; height: 50px; display: grid; place-items: center; border-radius: 15px; background: rgba(37, 213, 242, 0.10); font-size: 22px; }

        /* Allow the title area to use the remaining header width. */
        .drawer-title { flex: 1; }

        /* Style the system category above the main title. */
        .eyebrow { color: var(--cyan); font-size: 10px; font-weight: 900; letter-spacing: 0.16em; }

        /* Style the selected area name. */
        .drawer-title h2 { margin: 4px 0; font-size: 23px; }

        /* Style the selected area description. */
        .drawer-title p { margin: 4px 0 0; color: var(--muted); font-size: 11px; line-height: 1.5; }

        /* Style the drawer close button. */
        .close { width: 35px; height: 35px; border: 1px solid var(--border); border-radius: 10px; color: white; background: rgba(255, 255, 255, 0.04); font-size: 19px; cursor: pointer; }

        /* Make the drawer content independently scrollable. */
        .drawer-body { height: calc(100% - 112px); overflow: auto; padding: 18px; }

        /* Highlight the critical operating requirement. */
        .critical { padding: 11px; border: 1px solid rgba(255, 101, 123, 0.25); border-radius: 12px; color: #ffd5dc; background: rgba(255, 101, 123, 0.07); font-size: 12px; }

        /* Style section headings inside the drawer. */
        .section-title { margin: 18px 0 8px; color: var(--muted); font-size: 10px; font-weight: 900; letter-spacing: 0.14em; }

        /* Style each product or system-component card. */
        .product { margin: 9px 0; padding: 13px; border: 1px solid rgba(255, 255, 255, 0.09); border-radius: 14px; background: rgba(255, 255, 255, 0.028); }

        /* Highlight a product card when hovered. */
        .product:hover { border-color: rgba(37, 213, 242, 0.36); background: rgba(37, 213, 242, 0.04); }

        /* Style the product category pill. */
        .tag { float: right; padding: 4px 7px; border-radius: 99px; color: var(--green); background: rgba(67, 226, 159, 0.08); font-size: 9px; font-weight: 900; }

        /* Style product details. */
        .product ul { margin: 8px 0 0; padding-left: 17px; color: var(--muted); font-size: 10px; line-height: 1.55; }

        /* Style the final action button. */
        .cta { width: 100%; margin-top: 12px; padding: 12px; border: 0; border-radius: 12px; color: #04111c; background: linear-gradient(135deg, var(--cyan), #5d7fff); font-weight: 900; cursor: pointer; }

        /* Adapt the layout when the display is narrow. */
        @media (max-width: 900px) {
            .filters, .quick-links { display: none; }
            .visual { inset: 0; }
            .stage { inset: 76px 5px 5px; }
            .header { top: 10px; left: 10px; }
            .brand p { display: none; }
            .brand h1 { font-size: 16px; }
            .floor-panel { top: 10px; right: 10px; }
            .drawer { top: 80px; right: 8px; bottom: 8px; }
        }
    </style>
</head>
<body>
    <!-- Wrap the full interactive experience. -->
    <main class="app">
        <!-- Display the title and global system filters. -->
        <header class="header">
            <div class="brand glass">
                <h1>Overview</h1>
                <h4>Select to explore solution that electrifies, automates and digitizes</h4>
            </div>

            <nav class="filters glass" aria-label="System filters">
                <button class="active" onclick="showAll(this)">Overview</button>
                <button onclick="filterSystem('power', this)">Power</button>
                <button onclick="filterSystem('hvac', this)">HVAC</button>
                <button onclick="filterSystem('gas', this)">Medical gases</button>
            </nav>
        </header>

        <!-- Contain the hospital visualization and navigation overlays. -->
        <section class="stage">
            <!-- Render the hospital as a scalable, self-contained SVG illustration. -->
            <div class="visual">
                <svg viewBox="0 0 1120 720" role="img" aria-label="Multi-floor hospital with critical infrastructure">
                    <!-- Define gradients and shadows used by the illustration. -->
                    <defs>
                        <linearGradient id="buildingFront" x2="0" y2="1"><stop stop-color="#c7dce3"/><stop offset="1" stop-color="#55798b"/></linearGradient>
                        <linearGradient id="buildingSide"><stop stop-color="#789cab"/><stop offset="1" stop-color="#35596d"/></linearGradient>
                        <linearGradient id="buildingRoof"><stop stop-color="#f5fafc"/><stop offset="1" stop-color="#94b1bf"/></linearGradient>
                        <linearGradient id="campus"><stop stop-color="#193e56"/><stop offset="1" stop-color="#092034"/></linearGradient>
                        <filter id="shadow"><feDropShadow dy="15" stdDeviation="16" flood-opacity="0.52"/></filter>
                    </defs>

                    <!-- Paint the visual background. -->
                    <rect width="1120" height="720" fill="#0a2337"/>

                    <!-- Draw the isometric hospital campus base. -->
                    <path d="M80 470 L500 225 L1040 480 L615 705 Z" fill="url(#campus)" stroke="#67e7f52c" filter="url(#shadow)"/>

                    <!-- Draw the access road. -->
                    <path d="M130 530 L565 275 L972 470 L538 706" fill="none" stroke="#102a3d" stroke-width="62" stroke-linecap="round"/>

                    <!-- Add a dashed road center line. -->
                    <path d="M130 530 L565 275 L972 470 L538 706" fill="none" stroke="#a5bdc866" stroke-width="2" stroke-dasharray="11 13"/>

                    <!-- Draw the rooftop and HVAC floor. -->
                    <g class="floor" data-floor="4">
                        <g class="zone" data-zone="hvac">
                            <path class="surface" d="M344 188 L595 308 L595 350 L344 230 Z" fill="url(#buildingFront)"/>
                            <path class="surface" d="M595 308 L818 181 L818 223 L595 350 Z" fill="url(#buildingSide)"/>
                            <path class="surface" d="M344 188 L565 63 L818 181 L595 308 Z" fill="url(#buildingRoof)" stroke="#eaffff88"/>
                            <text x="371" y="215" class="floor-label">ROOF · HVAC PLANT</text>

                            <!-- Draw two animated rooftop AHU fan symbols. -->
                            <g transform="translate(500 132)">
                                <rect width="76" height="42" rx="5" fill="#2e6377" stroke="#64e9ff"/>
                                <circle class="fan" cx="22" cy="21" r="13" fill="none" stroke="#b8f7ff" stroke-width="3" stroke-dasharray="9 5"/>
                                <circle class="fan" cx="54" cy="21" r="13" fill="none" stroke="#b8f7ff" stroke-width="3" stroke-dasharray="9 5"/>
                            </g>

                            <!-- Draw the rooftop chiller or heat-pump placeholder. -->
                            <g transform="translate(625 145)">
                                <rect width="82" height="44" rx="5" fill="#2e6377" stroke="#64e9ff"/>
                                <path d="M9 11 H73 M9 22 H73 M9 33 H73" stroke="#8feeff"/>
                            </g>

                            <!-- Draw the rooftop helipad. -->
                            <circle cx="576" cy="168" r="39" fill="#27495a" stroke="white" stroke-width="3"/>
                            <text x="576" y="180" text-anchor="middle" font-size="35" font-weight="900" fill="white">H</text>
                        </g>
                    </g>

                    <!-- Draw Level 3 for operation theatres and critical care. -->
                    <g class="floor" data-floor="3">
                        <g class="zone" data-zone="ot">
                            <path class="surface" d="M344 230 L595 350 L595 423 L344 303 Z" fill="url(#buildingFront)"/>
                            <path class="surface" d="M595 350 L818 223 L818 296 L595 423 Z" fill="url(#buildingSide)"/>
                            <path class="surface" d="M365 240 L468 289 L468 340 L365 291 Z" fill="#31d7ff35" stroke="#65e8ff"/>
                            <path class="surface" d="M484 297 L575 340 L575 391 L484 348 Z" fill="#31d7ff26" stroke="#65e8ff"/>
                            <text x="371" y="270" class="floor-label">LEVEL 3 · OT & CRITICAL CARE</text>
                        </g>
                    </g>

                    <!-- Draw Level 2 for ICU and patient wards. -->
                    <g class="floor" data-floor="2">
                        <g class="zone" data-zone="icu">
                            <path class="surface" d="M344 303 L595 423 L595 496 L344 376 Z" fill="url(#buildingFront)"/>
                            <path class="surface" d="M595 423 L818 296 L818 369 L595 496 Z" fill="url(#buildingSide)"/>
                            <path class="surface" d="M365 313 L468 362 L468 413 L365 364 Z" fill="#ff657b35" stroke="#ff8da0"/>
                            <path class="surface" d="M484 370 L575 413 L575 464 L484 421 Z" fill="#43e29f28" stroke="#72efb7"/>
                            <text x="371" y="343" class="floor-label">LEVEL 2 · ICU & PATIENT WARDS</text>
                        </g>
                    </g>

                    <!-- Draw Level 1 for diagnostics and maternity. -->
                    <g class="floor" data-floor="1">
                        <g class="zone" data-zone="diagnostics">
                            <path class="surface" d="M344 376 L595 496 L595 569 L344 449 Z" fill="url(#buildingFront)"/>
                            <path class="surface" d="M595 496 L818 369 L818 442 L595 569 Z" fill="url(#buildingSide)"/>
                            <path class="surface" d="M365 386 L468 435 L468 486 L365 437 Z" fill="#a78bfa32" stroke="#c0adff"/>
                            <path class="surface" d="M484 443 L575 486 L575 537 L484 494 Z" fill="#ffbd592b" stroke="#ffd184"/>
                            <text x="371" y="416" class="floor-label">LEVEL 1 · DIAGNOSTICS & MATERNITY</text>
                        </g>
                    </g>

                    <!-- Draw the ground floor and the UPS/electrical room. -->
                    <g class="floor" data-floor="0">
                        <g class="zone" data-zone="ups">
                            <path class="surface" d="M344 449 L595 569 L595 630 L344 510 Z" fill="#375e70"/>
                            <path class="surface" d="M595 569 L818 442 L818 503 L595 630 Z" fill="#294b5d"/>
                            <path class="surface" d="M382 466 L469 508 L469 549 L382 507 Z" fill="#5b8cff34" stroke="#83a6ff"/>
                            <path class="surface" d="M486 516 L570 556 L570 597 L486 557 Z" fill="#ffbd592c" stroke="#ffd47f"/>
                            <text x="371" y="482" class="floor-label">GROUND · EMERGENCY & ELECTRICAL</text>

                            <!-- Draw two UPS cabinet placeholders. -->
                            <g transform="translate(392 486)">
                                <rect width="21" height="37" fill="#274d63" stroke="#79e8ff"/>
                                <circle cx="10.5" cy="9" r="3" fill="#43e29f"/>
                                <path d="M5 18 H16 M5 24 H16 M5 30 H16" stroke="#79e8ff"/>
                            </g>
                            <g transform="translate(424 501)">
                                <rect width="21" height="37" fill="#274d63" stroke="#79e8ff"/>
                                <circle cx="10.5" cy="9" r="3" fill="#43e29f"/>
                                <path d="M5 18 H16 M5 24 H16 M5 30 H16" stroke="#79e8ff"/>
                            </g>
                        </g>
                    </g>

                    <!-- Draw the emergency entrance canopy. -->
                    <g class="zone" data-zone="emergency">
                        <path class="surface" d="M465 552 L584 609 L584 660 L465 603 Z" fill="#15384b"/>
                        <path class="surface" d="M584 609 L695 546 L695 597 L584 660 Z" fill="#0e2b3c"/>
                        <path class="surface" d="M465 552 L576 489 L695 546 L584 609 Z" fill="#1dc8e3" stroke="#a3f4ff" stroke-width="2"/>
                    </g>

                    <!-- Draw the external utility yard. -->
                    <g class="zone" data-zone="utilities">
                        <path class="surface" d="M821 506 L930 558 L930 617 L821 565 Z" fill="#345a6d"/>
                        <path class="surface" d="M930 558 L1022 505 L1022 564 L930 617 Z" fill="#244659"/>
                        <path class="surface" d="M821 506 L913 453 L1022 505 L930 558 Z" fill="#7899a8"/>
                    </g>

                    <!-- Draw bulk medical oxygen storage tanks. -->
                    <g class="zone" data-zone="oxygen">
                        <g transform="translate(892 430)">
                            <ellipse cx="0" cy="0" rx="15" ry="8" fill="#e9fbff"/>
                            <rect x="-15" width="30" height="48" fill="#b8d1dc"/>
                            <ellipse cy="48" rx="15" ry="8" fill="#789baa"/>
                            <text x="-7" y="31" font-size="11" font-weight="900" fill="#173948">O₂</text>
                        </g>
                        <g transform="translate(934 452)">
                            <ellipse cx="0" cy="0" rx="12" ry="7" fill="#e9fbff"/>
                            <rect x="-12" width="24" height="40" fill="#b8d1dc"/>
                            <ellipse cy="40" rx="12" ry="7" fill="#789baa"/>
                        </g>
                    </g>

                    <!-- Draw the service-air compressor package. -->
                    <g class="zone" data-zone="air" transform="translate(780 565)">
                        <rect class="surface" width="64" height="36" rx="5" fill="#294f65" stroke="#ffbd59"/>
                        <circle cx="17" cy="18" r="10" fill="none" stroke="#ffd483" stroke-width="3"/>
                        <path d="M32 10 H55 M32 18 H55 M32 26 H55" stroke="#ffd483"/>
                    </g>

                    <!-- Draw animated resilient-power routes. -->
                    <g data-system="power">
                        <path class="flow" d="M410 513 C330 570 315 610 290 650" stroke="#5b8cff" stroke-width="5"/>
                        <path class="flow" d="M420 510 C500 460 545 430 600 390" stroke="#5b8cff" stroke-width="4"/>
                    </g>

                    <!-- Draw animated HVAC supply routes. -->
                    <g data-system="hvac">
                        <path class="flow" d="M625 152 C690 95 770 100 840 150" stroke="#25d5f2" stroke-width="5"/>
                        <path class="flow" d="M625 152 C620 255 610 330 606 465" stroke="#25d5f2" stroke-width="4"/>
                    </g>

                    <!-- Draw animated oxygen and service-air routes. -->
                    <g data-system="gas">
                        <path class="flow" d="M900 485 C820 430 750 390 680 350 C610 310 540 290 465 265" stroke="#43e29f" stroke-width="5"/>
                        <path class="flow" d="M810 580 C750 515 700 470 650 430" stroke="#ffbd59" stroke-width="5"/>
                    </g>

                    <!-- JavaScript inserts consistent clickable markers into this group. -->
                    <g id="markers"></g>
                </svg>
            </div>

            <!-- Provide floor-by-floor focus controls. -->
            <aside class="floor-panel glass">
                <h3>FLOOR FOCUS</h3>
                <div class="floor-buttons">
                    <button class="active" onclick="focusFloor('all', this)">ALL</button>
                    <button onclick="focusFloor('4', this)">ROOF</button>
                    <button onclick="focusFloor('3', this)">L3</button>
                    <button onclick="focusFloor('2', this)">L2</button>
                    <button onclick="focusFloor('1', this)">L1</button>
                    <button onclick="focusFloor('0', this)">GROUND</button>
                </div>
            </aside>

            <!-- Provide one-click access to the major engineering systems. -->
            <aside class="quick-links glass">
                <h3>Critical systems</h3>
                <button onclick="openZone('hvac')">Rooftop HVAC & AHU plant</button>
                <button onclick="openZone('ups')">Electrical room & UPS</button>
                <button onclick="openZone('oxygen')">Medical O₂ system</button>
                <button onclick="openZone('air')">Service air</button>
                <button onclick="openZone('icu')">ICU critical infrastructure</button>
                <button onclick="openZone('ot')">Operation Theatre systems</button>
            </aside>
        </section>

        <!-- Display detailed information for the selected system or hospital zone. -->
        <aside class="drawer" id="drawer">
            <div class="drawer-header">
                <div class="system-icon" id="systemIcon">⚡</div>
                <div class="drawer-title">
                    <div class="eyebrow" id="eyebrow">CRITICAL INFRASTRUCTURE</div>
                    <h2 id="systemTitle">Hospital System</h2>
                    <p id="systemDescription"></p>
                </div>
                <button class="close" id="closeButton" aria-label="Close details">×</button>
            </div>

            <div class="drawer-body">
                <div class="critical" id="criticalRequirement"></div>
                <div class="section-title">SYSTEM COMPONENTS / PRODUCTS</div>
                <div id="productList"></div>
                <button class="cta" onclick="alert('Placeholder: This button to be connected to product detail page or enquiry workflow.')">Explore complete solution</button>
            </div>
        </aside>
    </main>

    <script>
        // Store all zone descriptions and placeholder products in one editable object.
        const ZONES = {
            hvac: {
                name: "HVAC & AHU Plant",
                icon: "❄",
                type: "ROOF · MECHANICAL",
                description: "Central air-handling and cooling infrastructure serving operation theatres, ICU, and wards.",
                critical: "Continuous airflow, filtration, temperature, humidity, and pressure control",
                products: [
                    ["Air Handling Unit", "HVAC", ["Supply and return fans control using xD Series drives", ""]],
                    ["Chiller / Heat Pump", "COOLING", ["VFD Panel for control and automation", "Energy-efficiency monitoring"]],
                    ["HVAC Automation", "CONTROL", ["Environmental sensors - temperature, Humidity and Pressure", "SmartComm integration and alarms"]]
                ]
            },
            ups: {
                name: "Electrical & UPS Room",
                icon: "⚡",
                type: "GROUND · ELECTRICAL",
                description: "Resilient power backbone for clinical loads, controls, networks and medical equipment",
                critical: "No-break supply with source redundancy and selective protection with 100% Visibility",
                products: [
                    ["Redundant PCC", "POWER", ["2 Main PCCs configuration ", "IEC 61439 Design Verified Assembly"]],
                    ["Thermal Monitoring", "CONDITION MONITORING", ["24x7 Wireless Thermal Monitoring with TMZ", "Alarms for quick decision making before any suprises"]],
                    ["SmartComm Power Management Software", "DIGITAL", ["Power-quality event logs for maintaining equiptments health", "Wi-Fi enabled Energy management dashboards with SmartComm in a box"]]
                ]
            },
            oxygen: {
                name: "Medical Oxygen System",
                icon: "O₂",
                type: "UTILITY YARD · MEDICAL GAS",
                description: "Bulk oxygen storage, pressure regulation, and piped distribution to clinical areas.",
                critical: "Continuous regulated oxygen supply with reserve and alarm supervision",
                products: [
                    ["Oxygen Storage", "STORAGE", ["Primary and reserve source monitoring using xP6000 PLC", "Level and pressure monitoring using xP6000 PLC"]],
                    ["Manifold & Regulators", "CONTROL", ["Control using xD Series VFDs", "Closed-loop Pressure regulation"]],
                    ["Area Alarm Panels", "ALARM", ["High and low pressure alarms for immediate addressal in Local", "Remote status integration in SmartComm"]]
                ]
            },
            air: {
                name: "Medical Service Air",
                icon: "AIR",
                type: "UTILITY YARD · MEDICAL GAS",
                description: "Oil-free compressed-air system supplying clinical service-air outlets throughout the hospital.",
                critical: "Clean, dry, and continuously available medical air",
                products: [
                    ["Oil-Free Compressor", "GENERATION", ["Duty and standby arrangement", "Runtime and fault monitoring"]],
                    ["Dryer & Receiver", "TREATMENT", ["Moisture-removal placeholder", "Pressure stabilization"]],
                    ["Air Distribution", "NETWORK", ["Ring-main piping", "Zone valves and alarms"]]
                ]
            },
            icu: {
                name: "Intensive Care Unit",
                icon: "❤",
                type: "LEVEL 2 · CLINICAL",
                description: "Continuous life-support, monitoring, and medical-gas availability for high-acuity care.",
                critical: "Highest uptime and power-quality priority",
                products: [
                    ["Critical Power Distribution", "POWER", ["Essential circuits loop monitoring to monitor system earthing in IT systems", "Selective protection and monitoring"]],
                    ["Bed-head Monitoring", "DIGITAL", ["Real-time alarms", "Energy and environmental data"]],
                    ["Medical Gas Outlets", "MEDICAL GAS", ["Oxygen and service-air terminal units monitoring", "Zone monitoring and alarms"]]
                ]
            },
            ot: {
                name: "Operation Theatre",
                icon: "✚",
                type: "LEVEL 3 · CLINICAL",
                description: "Controlled surgical environment requiring isolated power, clean air, and reliable medical gases.",
                critical: "Isolated supply, pressure control, and continuous monitoring",
                products: [
                    ["Isolated Power System", "POWER", ["Isolation-transformer ", "Insulation monitoring device IMR"]],
                    ["OT HVAC Control", "HVAC", ["HEPA-filtration VFD", "Pressure and temperature control"]],
                    ["Medical Gas Manifold", "MEDICAL GAS", ["Oxygen and service-air distribution control", ""]]
                ]
            },
            diagnostics: {
                name: "Diagnostics & Imaging",
                icon: "◉",
                type: "LEVEL 1 · CLINICAL",
                description: "Imaging and diagnostic equipment requiring stable power and controlled environmental conditions.",
                critical: "Voltage stability, harmonic control, and equipment availability",
                products: [
                    ["Power Quality Solution", "POWER", ["Harmonic, PQ Events & transient monitoring to protect lab equiptments", "Equipment-feeder metering"]],
                    ["Room Environment Control", "HVAC", ["Temperature stability", "Equipment heat-load management"]],
                    ["Digital Monitoring", "DIGITAL", ["Alerts and maintenance analytics", "Asset-performance integration"]]
                ]
            },
            emergency: {
                name: "Emergency Department",
                icon: "✚",
                type: "GROUND · CLINICAL",
                description: "Rapid-response clinical zone connected to emergency power and essential utilities.",
                critical: "Fast source transfer and immediate fault visibility",
                products: [
                    ["Automatic Transfer", "POWER", ["Normal and emergency source changeover", "Status and event indication"]],
                    ["Emergency Panel", "DISTRIBUTION", ["Critical-circuit segregation", "Selective protection"]],
                    ["Facility Alerts", "DIGITAL", ["Alarm-escalation hierarchy/matrix", "Integrated facility dashboard"]]
                ]
            },
            utilities: {
                name: "Central Utility Yard",
                icon: "⚙",
                type: "EXTERNAL · ENGINEERING",
                description: "Centralized engineering infrastructure for power, HVAC, oxygen, and service air.",
                critical: "Redundancy, maintainability, and remote supervision",
                products: [
                    ["Utility Control Panel", "CONTROL", ["Integrated equipment control", "Remote I/O and communications"]],
                    ["Energy & Utility Metering", "DIGITAL", ["Electrical and mechanical consumption", "Trend and alarm dashboards"]],
                    ["Condition Monitoring", "SERVICE", ["Predictive-maintenance inputs", "Asset-health reporting"]]
                ]
            }
        };

        // Define each marker's zone key, position, label, and color.
        const MARKERS = [
            ["hvac", 620, 112, "HVAC", "#25d5f2"],
            ["ot", 720, 242, "OT", "#25d5f2"],
            ["icu", 420, 355, "ICU", "#ff657b"],
            ["diagnostics", 425, 430, "Diagnostics", "#a78bfa"],
            ["ups", 365, 552, "Electrical & UPS Room", "#5b8cff"],
            ["oxygen", 930, 412, "Oxygen", "#43e29f"],
            ["air", 792, 627, "Service Air", "#ffbd59"],
            ["emergency", 570, 520, "Emergency", "#ff657b"]
        ];

        // Get the SVG group that will contain all generated markers.
        const markerLayer = document.getElementById("markers");

        // Build consistent marker graphics from the marker configuration.
        markerLayer.innerHTML = MARKERS.map((marker, index) => {
            // Read the marker configuration into descriptive variables.
            const [key, x, y, label, color] = marker;

            // Place labels on the left when the marker is near the right edge.
            const labelOffset = x > 820 ? -120 : 29;

            // Calculate a label width based on the amount of text.
            const labelWidth = Math.max(70, label.length * 7 + 24);

            // Return one clickable SVG group.
            return `
                <g class="zone" data-zone="${key}">
                    <g class="pin">
                        <circle cx="${x}" cy="${y}" r="25" fill="${color}" opacity="0.18"/>
                        <circle cx="${x}" cy="${y}" r="18" fill="${color}" stroke="white" stroke-width="3"/>
                        <text x="${x}" y="${y + 4}" text-anchor="middle" font-size="11" font-weight="900" fill="#04111c">${index + 1}</text>
                        <rect x="${x + labelOffset}" y="${y - 16}" width="${labelWidth}" height="31" rx="9" fill="#051421ef" stroke="#ffffff23"/>
                        <text x="${x + labelOffset + 11}" y="${y + 4}" class="marker-label">${label}</text>
                    </g>
                </g>
            `;
        }).join("");

        // Cache the drawer element for repeated use.
        const drawer = document.getElementById("drawer");

        // Open the detail drawer for a selected hospital zone.
        function openZone(key) {
            // Look up the selected zone's content.
            const zone = ZONES[key];

            // Stop if a malformed element has no matching data.
            if (!zone) return;

            // Highlight every SVG element linked to the selected zone.
            document.querySelectorAll(".zone").forEach((element) => {
                element.classList.toggle("active", element.dataset.zone === key);
            });

            // Populate the drawer icon.
            document.getElementById("systemIcon").textContent = zone.icon;

            // Populate the drawer category.
            document.getElementById("eyebrow").textContent = zone.type;

            // Populate the drawer title.
            document.getElementById("systemTitle").textContent = zone.name;

            // Populate the drawer description.
            document.getElementById("systemDescription").textContent = zone.description;

            // Populate the critical operating requirement.
            document.getElementById("criticalRequirement").textContent = `● ${zone.critical}`;

            // Convert each product entry into a product card.
            document.getElementById("productList").innerHTML = zone.products.map((product) => {
                // Read product fields into descriptive variables.
                const [name, category, details] = product;

                // Return one product card with a bullet list.
                return `
                    <article class="product">
                        <span class="tag">${category}</span>
                        <b>${name}</b>
                        <ul>${details.map((detail) => `<li>${detail}</li>`).join("")}</ul>
                    </article>
                `;
            }).join("");

            // Move the drawer into view.
            drawer.classList.add("open");
        }

        // Attach click handlers after generated markers are present.
        document.querySelectorAll(".zone").forEach((element) => {
            element.addEventListener("click", (event) => {
                // Prevent a nested zone click from reaching its parent zone.
                event.stopPropagation();

                // Open the zone linked through the data-zone attribute.
                openZone(element.dataset.zone);
            });
        });

        // Close the drawer when the close button is selected.
        document.getElementById("closeButton").addEventListener("click", () => {
            // Hide the drawer.
            drawer.classList.remove("open");

            // Remove selected-state highlighting from all zones.
            document.querySelectorAll(".zone").forEach((element) => element.classList.remove("active"));
        });

        // Focus on one floor while dimming the remaining floors.
        function focusFloor(floor, selectedButton) {
            // Update the selected floor button.
            document.querySelectorAll(".floor-buttons button").forEach((button) => button.classList.remove("active"));
            selectedButton.classList.add("active");

            // Dim every floor except the requested floor.
            document.querySelectorAll(".floor").forEach((element) => {
                element.classList.toggle("dim", floor !== "all" && element.dataset.floor !== floor);
            });
        }

        // Emphasize one engineering route and open its most relevant system.
        function filterSystem(system, selectedButton) {
            // Update the active filter button.
            document.querySelectorAll(".filters button").forEach((button) => button.classList.remove("active"));
            selectedButton.classList.add("active");

            // Dim routes that do not belong to the selected engineering system.
            document.querySelectorAll("[data-system]").forEach((route) => {
                route.style.opacity = route.dataset.system === system ? "1" : "0.08";
            });

            // Map each filter to the most relevant detail panel.
            const defaultZone = { power: "ups", hvac: "hvac", gas: "oxygen" };

            // Open the corresponding detail panel.
            openZone(defaultZone[system]);
        }

        // Restore all route layers and close the detail drawer.
        function showAll(selectedButton) {
            // Update the active filter button.
            document.querySelectorAll(".filters button").forEach((button) => button.classList.remove("active"));
            selectedButton.classList.add("active");

            // Restore full opacity to every route layer.
            document.querySelectorAll("[data-system]").forEach((route) => route.style.opacity = "1");

            // Close the detail drawer to show the complete hospital.
            drawer.classList.remove("open");
        }
    </script>
</body>
</html>
'''

# Render the interactive HTML at a height suitable for laptop and presentation displays.
components.html(
    HTML,
    height=930,
    scrolling=False,
)