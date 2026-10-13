
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Riu | Nuestro pequeño universo",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* INTRODUCCIÓN: NACIMIENTO DEL UNIVERSO */

#cosmicIntro {
    position: absolute;
    inset: 0;
    z-index: 40;
    display: none;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: #03030d;
    opacity: 1;
    transition: opacity 2s ease;
}

#cosmicCore {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    background: white;
    box-shadow:
        0 0 25px #fff,
        0 0 65px #c89aff,
        0 0 120px #8a62ff;
}

.cosmicRing {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 80px;
    height: 80px;
    border: 2px solid #dcb5ff;
    border-radius: 50%;
    transform: translate(-50%, -50%) scale(.1);
    opacity: 0;
}

#cosmicIntro.expand #cosmicCore {
    animation: coreExpand 6s ease-in forwards;
}

#cosmicIntro.expand .cosmicRing {
    animation: ringExpand 5s ease-out forwards;
}

#cosmicIntro.expand .ring2 {
    animation-delay: .7s;
}

#cosmicIntro.expand .ring3 {
    animation-delay: 1.4s;
}

@keyframes coreExpand {
    0% {
        transform: translate(-50%, -50%) scale(.5);
        opacity: 1;
    }
    35% {
        transform: translate(-50%, -50%) scale(3);
    }
    100% {
        transform: translate(-50%, -50%) scale(80);
        opacity: 0;
    }
}

@keyframes ringExpand {
    0% {
        transform: translate(-50%, -50%) scale(.1);
        opacity: 0;
    }
    20% { opacity: .9; }
    100% {
        transform: translate(-50%, -50%) scale(16);
        opacity: 0;
    }
}

#cosmicText {
    position: absolute;
    left: 5%;
    width: 90%;
    top: 70%;
    text-align: center;
    color: #f7e8ff;
    font-size: clamp(15px, 2.5vw, 22px);
    letter-spacing: 3px;
    opacity: 0;
    text-shadow: 0 0 20px #d8a8ff;
}

#cosmicIntro.expand #cosmicText {
    animation: cosmicTextFade 4s ease forwards;
    animation-delay: .8s;
}

@keyframes cosmicTextFade {
    0% { opacity: 0; transform: translateY(12px); }
    30%, 75% { opacity: 1; transform: translateY(0); }
    100% { opacity: 0; transform: translateY(-10px); }
}

.stApp {
    background: #0c0a19;
}
header, footer, #MainMenu {
    visibility: hidden;
}
.block-container {
    padding: 0.5rem 0.7rem;
    max-width: 1200px;
}
</style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #0c0a19;
    color: white;
    font-family: Georgia, serif;
}

button, input {
    font-family: inherit;
}

#world {
    width: 100%;
    height: 720px;
    position: relative;
    overflow: hidden;
    isolation: isolate;
    border: 1px solid #79558e;
    border-radius: 24px;
    background:
        radial-gradient(ellipse at 50% 110%,
            #8b456f 0%, transparent 48%),
        radial-gradient(ellipse at 75% 20%,
            #393271 0%, transparent 45%),
        linear-gradient(180deg,
            #090d24 0%, #211538 58%, #392344 100%);
}

/* UNIVERSO */

#nebula {
    position: absolute;
    inset: -20%;
    z-index: -1;
    background:
        radial-gradient(ellipse at 25% 45%,
            #9f5cd855, transparent 25%),
        radial-gradient(ellipse at 70% 35%,
            #697ce044, transparent 28%),
        radial-gradient(ellipse at 50% 75%,
            #ee6bba30, transparent 32%);
    animation: nebulaMove 18s ease-in-out infinite alternate;
}

@keyframes nebulaMove {
    from { transform: rotate(-7deg) scale(1); }
    to { transform: rotate(7deg) scale(1.18); }
}

#starfield {
    position: absolute;
    inset: 0;
    z-index: 1;
    pointer-events: none;
}

.star {
    position: absolute;
    color: #fff2e0;
    text-shadow: 0 0 12px #fff5dd;
    animation: shimmer 2.5s ease-in-out infinite alternate;
}

@keyframes shimmer {
    from {
        opacity: .25;
        transform: scale(.7);
    }
    to {
        opacity: 1;
        transform: scale(1.2);
    }
}

#moon {
    position: absolute;
    top: 38px;
    right: 12%;
    width: 62px;
    height: 62px;
    border-radius: 50%;
    background: #fff0cf;
    box-shadow: 0 0 40px #ffe9bd77;
    z-index: 1;
}

#moon:after {
    content: "";
    position: absolute;
    width: 55px;
    height: 55px;
    top: -7px;
    left: 20px;
    border-radius: 50%;
    background: #111029;
}

#shootingStar {
    position: absolute;
    top: 19%;
    left: -20%;
    width: 110px;
    height: 2px;
    opacity: 0;
    z-index: 3;
    transform: rotate(-20deg);
    background: linear-gradient(90deg,
        transparent, #fff, #ffc7e9, transparent);
    box-shadow: 0 0 12px #ffbce5;
}

@keyframes shooting {
    0% { left: -20%; opacity: 0; }
    10% { opacity: 1; }
    80% { opacity: 1; }
    100% { left: 115%; opacity: 0; }
}

/* PANTALLA DE CONTRASEÑA */

#gate {
    position: absolute;
    inset: 0;
    z-index: 50;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 18px;
    background: #0b0a1bed;
    backdrop-filter: blur(12px);
}

.gateCard {
    width: min(450px, 100%);
    padding: 30px 26px;
    text-align: center;
    border-radius: 25px;
    border: 1px solid #cf9ce377;
    background: linear-gradient(145deg,
        #302046f5, #17132bf5);
    box-shadow: 0 0 60px #d56ecb20;
}

.lock {
    font-size: 53px;
    margin-bottom: 10px;
}

.gateTitle {
    font-size: clamp(25px, 4vw, 36px);
    color: #ffe0ef;
    margin-bottom: 16px;
}

.gateText {
    color: #e4d2ef;
    line-height: 1.8;
    font-size: 16px;
}

#nickname {
    display: block;
    width: 100%;
    margin-top: 20px;
    padding: 14px;
    text-align: center;
    border: 1px solid #b78acb;
    border-radius: 13px;
    outline: none;
    background: #100d22;
    color: white;
    font-size: 18px;
}

#nickname:focus {
    border-color: #ffbfe1;
    box-shadow: 0 0 16px #ec8bc944;
}

#enter {
    width: 100%;
    padding: 14px;
    margin-top: 14px;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    font-size: 16px;
    color: #321a3b;
    background: linear-gradient(100deg,
        #ffd2e5, #d9bbff);
    transition: transform .2s, box-shadow .2s;
}

#enter:hover {
    transform: scale(1.025);
    box-shadow: 0 0 25px #efa5df55;
}

#error {
    color: #ffb6d0;
    font-size: 14px;
    margin-top: 12px;
    min-height: 20px;
}

/* ESCENARIO */

#ground {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 140px;
    z-index: 2;
    border-top: 1px solid #a16bb777;
    border-radius: 50% 50% 0 0 / 12% 12% 0 0;
    background: linear-gradient(180deg,
        #4a2d50cc, #17132a);
}

.character {
    position: absolute;
    bottom: 105px;
    z-index: 6;
    font-size: clamp(68px, 10vw, 100px);
    line-height: 1.15;
    user-select: none;
    filter: drop-shadow(0 0 16px #eaa7ef33);
}

#prince {
    left: -160px;
    transition: left 2.5s ease-in-out;
}

#princess {
    right: -160px;
    opacity: 0;
    transition: right 2.5s ease-in-out, opacity 1.5s;
}

#singing {
    position: absolute;
    left: 13%;
    bottom: 215px;
    z-index: 7;
    font-size: 27px;
    color: #ffd7ee;
    text-shadow: 0 0 18px #f38dd9;
    opacity: 0;
    transition: opacity 1s;
    animation: sing 1s ease-in-out infinite alternate;
}

@keyframes sing {
    from { transform: translateY(0) scale(1); }
    to { transform: translateY(-7px) scale(1.08); }
}

/* ROSA */

#rose {
    position: absolute;
    left: 48%;
    bottom: 125px;
    z-index: 8;
    font-size: 47px;
    opacity: 0;
    transform: translateX(-50%);
    filter: drop-shadow(0 0 14px #ff6e9b);
    transition:
        left 2s ease,
        bottom 1.5s ease,
        opacity 1.2s ease,
        transform 1.2s ease;
}

#roseGlow {
    position: absolute;
    left: 48%;
    bottom: 155px;
    z-index: 7;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background: #ff70b92a;
    filter: blur(12px);
    opacity: 0;
    transform: translateX(-50%);
    transition: opacity 1s;
}

/* TEXTOS */

#intro {
    position: absolute;
    z-index: 12;
    top: 10%;
    left: 5%;
    width: 90%;
    text-align: center;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 1.5s, transform 1.5s;
    text-shadow: 0 0 20px #f18bc7;
    pointer-events: none;
}

#intro h2 {
    font-size: clamp(23px, 4vw, 37px);
    font-weight: normal;
    color: #ffe1f1;
    margin: 0 0 12px;
}

#intro p {
    color: #e6d4f0;
    font-size: clamp(14px, 2vw, 18px);
    line-height: 1.7;
    margin: 0;
}

#final {
    position: absolute;
    z-index: 16;
    top: 30%;
    left: 0;
    width: 100%;
    text-align: center;
    opacity: 0;
    transform: scale(.6);
    transition: opacity 2.5s, transform 2.5s;
    pointer-events: none;
}

#final h1 {
    margin: 0;
    color: #fff1fa;
    font-size: clamp(48px, 10vw, 94px);
    font-weight: normal;
    letter-spacing: 7px;
    text-shadow:
        0 0 12px #ffbce7,
        0 0 35px #f76dcc,
        0 0 75px #ad65ff;
}

#final p {
    margin-top: 20px;
    color: #f7d8f0;
    font-size: clamp(17px, 3vw, 24px);
    font-style: italic;
}

#status {
    position: absolute;
    top: 5%;
    left: 5%;
    z-index: 14;
    color: #f4d8f2;
    font: 12px Arial, sans-serif;
    letter-spacing: 1px;
    opacity: .8;
}

/* REPRODUCTOR OFICIAL */

#musicPanel {
    position: absolute;
    z-index: 22;
    right: 12px;
    bottom: 12px;
    width: 235px;
    padding: 9px;
    border-radius: 14px;
    border: 1px solid #9f7abb77;
    background: #100d24e8;
    box-shadow: 0 0 20px #0005;
}

#musicLabel {
    text-align: center;
    font: 11px Arial, sans-serif;
    color: #f2cfe9;
    letter-spacing: 1px;
    margin: 2px 0 7px;
}

#player {
    width: 215px;
    height: 121px;
    overflow: hidden;
    border-radius: 8px;
}

#replay {
    position: absolute;
    z-index: 25;
    display: none;
    left: 50%;
    bottom: 20px;
    transform: translateX(-50%);
    padding: 12px 24px;
    color: white;
    border: 1px solid #eab9e3;
    border-radius: 25px;
    background: #70437fdc;
    cursor: pointer;
}

/* CORAZONES */

.heart {
    position: absolute;
    bottom: -35px;
    z-index: 13;
    pointer-events: none;
    animation: floatHeart 5s linear forwards;
}

@keyframes floatHeart {
    0% {
        transform: translateY(0) scale(.7);
        opacity: 0;
    }
    15% { opacity: 1; }
    100% {
        transform: translateY(-730px) rotate(35deg) scale(1.3);
        opacity: 0;
    }
}

@media (max-width: 600px) {
    #world { height: 760px; }
    .character { bottom: 140px; }
    #ground { height: 165px; }
    #musicPanel {
        width: 172px;
        right: 7px;
        bottom: 7px;
    }
    #player {
        width: 152px;
        height: 86px;
    }
    #intro { top: 9%; }
    #final { top: 28%; }
}
</style>
</head>

<body>
<div id="world">
<div id="cosmicIntro">
    <div id="cosmicCore"></div>
    <div class="cosmicRing ring1"></div>
    <div class="cosmicRing ring2"></div>
    <div class="cosmicRing ring3"></div>
    <div id="cosmicText">
        SOMEWHERE IN THIS UNIVERSE... ♡
    </div>
</div>
    <div id="nebula"></div>
    <div id="starfield"></div>
    <div id="moon"></div>
    <div id="shootingStar"></div>
    <div id="ground"></div>

    <!-- CONTRASEÑA -->
    <div id="gate">
        <div class="gateCard">
            <div class="lock">🌙 🔐</div>

            <div class="gateTitle">
                Una pequeña sorpresa...
            </div>

            <div class="gateText">
                Para asegurarme de que eres mi amada,
                ingresa tu apodo :3
                <br><br>
                <span style="color:#f5bde4">
                    Solo tú conoces la respuesta ♡
                </span>
            </div>

            <input
                id="nickname"
                type="password"
                placeholder="Escribe tu apodo..."
                autocomplete="off"
            >

            <button id="enter" onclick="checkPassword()">
                Abrir nuestra historia ✨
            </button>

            <div id="error"></div>
        </div>
    </div>

    <!-- HISTORIA -->
    <div id="status">NUESTRO PEQUEÑO UNIVERSO ✦</div>

    <div id="intro">
        <h2>¡Sabía que eras tú, mi princesa! ♡</h2>
        <p>
            Este pequeño universo es para ti.
            <br>
            Recuérdalo siempre.
        </p>
    </div>

    <div id="prince" class="character">🤴🏻</div>
    <div id="princess" class="character">👸🏻</div>
    <div id="singing">♪ ♫ ♪</div>

    <div id="roseGlow"></div>
    <div id="rose">🌹</div>

    <div id="final">
        <h1>TE AMO</h1>
        <p>Mi princesa, hoy y siempre. ♡</p>
    </div>

    <!-- Videoclip oficial de YouTube -->
    <div id="musicPanel">
        <div id="musicLabel">♫ NUESTRA CANCIÓN ♫</div>
        <div id="player"></div>
    </div>

    <button id="replay" onclick="restartStory()">
        ↻ Volver a vivirlo
    </button>
</div>

<script>
/* CONFIGURACIÓN */

const VIDEO_ID = "gO8-9OWzPOQ";
const MUSIC_START = 30;
const MUSIC_END = 90;
const STORY_DURATION = (MUSIC_END - MUSIC_START) * 1000;

let player = null;
let playerReady = false;
let timers = [];
let heartInterval = null;
let storyToken = 0;

/* ESTRELLAS */

const starfield = document.getElementById("starfield");

for (let i = 0; i < 100; i++) {
    const star = document.createElement("span");
    star.className = "star";
    star.textContent = Math.random() > 0.65 ? "✦" : "·";
    star.style.left = Math.random() * 100 + "%";
    star.style.top = Math.random() * 100 + "%";
    star.style.fontSize = (8 + Math.random() * 13) + "px";
    star.style.animationDelay = Math.random() * 4 + "s";
    star.style.animationDuration = (1.5 + Math.random() * 3) + "s";
    starfield.appendChild(star);
}

/* REPRODUCTOR DE YOUTUBE */

function onYouTubeIframeAPIReady() {
    player = new YT.Player("player", {
        width: "215",
        height: "121",
        videoId: VIDEO_ID,
        playerVars: {
            autoplay: 0,
            controls: 1,
            playsinline: 1,
            rel: 0,
            start: MUSIC_START,
            end: MUSIC_END
        },
        events: {
            onReady: function() {
                playerReady = true;
                document.getElementById("error").textContent = "";
            },
            onError: function() {
                document.getElementById("error").textContent =
                    "YouTube no pudo cargar el videoclip. Comprueba tu conexión.";
            }
        }
    });
}

const ytScript = document.createElement("script");
ytScript.src = "https://www.youtube.com/iframe_api";
document.head.appendChild(ytScript);

/* UTILIDADES */

function later(callback, delay, token) {
    const id = setTimeout(() => {
        if (token === storyToken) callback();
    }, delay);
    timers.push(id);
}

function clearTimers() {
    timers.forEach(clearTimeout);
    timers = [];

    if (heartInterval) {
        clearInterval(heartInterval);
        heartInterval = null;
    }
}

function showHearts() {
    const heart = document.createElement("div");
    heart.className = "heart";

    const options = ["♡", "♥", "💗", "✧", "💕"];
    heart.textContent = options[
        Math.floor(Math.random() * options.length)
    ];

    heart.style.left = (5 + Math.random() * 90) + "%";
    heart.style.color = [
        "#ffc3e3", "#fff0f8", "#e8b8ff", "#ff9fbf"
    ][Math.floor(Math.random() * 4)];

    heart.style.fontSize = (17 + Math.random() * 20) + "px";
    heart.style.animationDuration = (4 + Math.random() * 3) + "s";

    document.getElementById("world").appendChild(heart);

    setTimeout(() => heart.remove(), 7500);
}

function resetScene() {
    const prince = document.getElementById("prince");
    const princess = document.getElementById("princess");
    const rose = document.getElementById("rose");

    prince.style.transition = "none";
    prince.style.left = "-160px";

    princess.style.transition = "none";
    princess.style.right = "-160px";
    princess.style.opacity = "0";

    rose.style.transition = "none";
    rose.style.left = "48%";
    rose.style.bottom = "125px";
    rose.style.opacity = "0";
    rose.style.transform = "translateX(-50%)";

    document.getElementById("roseGlow").style.opacity = "0";
    document.getElementById("singing").style.opacity = "0";

    document.getElementById("intro").style.opacity = "0";
    document.getElementById("intro").style.transform = "translateY(12px)";

    document.getElementById("final").style.opacity = "0";
    document.getElementById("final").style.transform = "scale(.6)";

    document.getElementById("replay").style.display = "none";

    document.querySelectorAll(".heart").forEach(h => h.remove());

    void prince.offsetWidth;

    prince.style.transition = "left 2.5s ease-in-out";
    princess.style.transition =
        "right 2.5s ease-in-out, opacity 1.5s";

    rose.style.transition =
        "left 2s ease, bottom 1.5s ease, opacity 1.2s ease";
}

/* CONTRASEÑA */


function checkPassword() {
    const input = document.getElementById("nickname");
    const error = document.getElementById("error");

    if (input.value !== "Riu") {
        error.textContent =
            "Mmm... ese no es. Inténtalo otra vez :3";
        input.value = "";
        input.focus();
        return;
    }

    if (!playerReady || !player) {
        error.textContent =
            "El universo se está preparando. Espera un instante ♡";
        return;
    }

    error.textContent = "";
    document.getElementById("gate").style.display = "none";

    const intro = document.getElementById("cosmicIntro");
    intro.style.display = "flex";
    intro.style.opacity = "1";

    // La canción comienza exactamente en el segundo 30.
    player.seekTo(30, true);
    player.playVideo();

    // El universo empieza a expandirse al comenzar la música.
    requestAnimationFrame(() => {
        intro.classList.add("expand");
    });

    // A los 6 segundos, el universo deja paso a la historia.
    setTimeout(() => {
        intro.style.opacity = "0";

        setTimeout(() => {
            intro.style.display = "none";
            startStory(false);
        }, 1800);
    }, 6000);
}

/* HISTORIA DE 60 SEGUNDOS */

function startStory(playMusic = true) {
    clearTimers();
    storyToken++;

    const token = storyToken;

    resetScene();

    // 0–6 s: bienvenida y estrellas fugaces.
    later(() => {
        const intro = document.getElementById("intro");
        intro.style.opacity = "1";
        intro.style.transform = "translateY(0)";

        const shooting = document.getElementById("shootingStar");
        shooting.style.animation = "none";
        void shooting.offsetWidth;
        shooting.style.animation = "shooting 2.5s ease-in-out forwards";
    }, 200, token);

    // 5–13 s: entra el príncipe.
    later(() => {
        document.getElementById("prince").style.left = "17%";
        document.getElementById("singing").style.opacity = "1";
    }, 5000, token);

    // 12–20 s: aparece la princesa.
    later(() => {
        document.getElementById("princess").style.right = "17%";
        document.getElementById("princess").style.opacity = "1";
    }, 12000, token);

    // 19–28 s: la rosa aparece mágicamente.
    later(() => {
        document.getElementById("rose").style.opacity = "1";
        document.getElementById("roseGlow").style.opacity = "1";
    }, 19000, token);

    // 27–36 s: el príncipe se acerca.
    later(() => {
        document.getElementById("prince").style.left = "43%";
        document.getElementById("rose").style.left = "57%";
        document.getElementById("rose").style.bottom = "205px";
    }, 27000, token);

    // 36–44 s: entrega de la rosa.
    later(() => {
        document.getElementById("rose").style.left = "70%";
        document.getElementById("rose").style.bottom = "225px";
        document.getElementById("roseGlow").style.opacity = "1";
    }, 36000, token);

    // 44–51 s: el universo se llena de corazones.
    later(() => {
        document.getElementById("intro").style.opacity = "0";
        document.getElementById("singing").style.opacity = "0";

        heartInterval = setInterval(showHearts, 300);
    }, 44000, token);

    // 51–60 s: declaración final.
    later(() => {
        if (heartInterval) {
            clearInterval(heartInterval);
            heartInterval = null;
        }

        const finalMessage = document.getElementById("final");
        finalMessage.style.opacity = "1";
        finalMessage.style.transform = "scale(1)";

        document.getElementById("replay").style.display = "block";
    }, 51000, token);

    // A los 60 s de historia, detener la música.
    later(() => {
        if (playMusic) {
    player.seekTo(30, true);
    player.playVideo();
}
    }, STORY_DURATION, token);
}

/* VOLVER A EMPEZAR */

function restartStory() {
    if (!playerReady || !player) return;

    // El clic permite reanudar el audio.
    player.seekTo(MUSIC_START, true);
    player.playVideo();

    startStory();
}
</script>
</body>
</html>
"""

components.html(html, height=740, scrolling=False)