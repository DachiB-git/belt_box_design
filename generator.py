# pip3 install requests
import requests

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
# Retrieve these from https://htmlcsstoimage.com/dashboard
HCTI_API_USER_ID = '4ca005f0-183e-4480-a324-b39590bed5ce'
HCTI_API_KEY = '1bf562e1-9793-4807-9d9f-4b8a49767228'

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="./index.css" />
  </head>
  <body>
    <div id="container">
      <div id="left">
        <h1></h1>
        <div id="recycle-container">
          <img class="recycle" src="./recycable.png" alt="pulley system" />
          <img
            class="recycle"
            src="./triangular-arrows-sign-for-recycle.png"
            alt="pulley system"
          />
        </div>
      </div>
      <div id="front">
        <h1>
          <p>VECTOR</p>
        </h1>
        <ul>
          <li>Keilrippenriemen</li>
          <li>Ribbed V-belt</li>
          <li>Courroie striée</li>
          <li>Multi V-riem</li>
          <li>Cinghia trapezoidale</li>
          <li>nervata</li>
          <li>Correa nervada</li>
          <li>Correia estriada</li>
          <li>Fortandet rem</li>
          <li>Поликлиновой ремень</li>
          <li>Oluklu V kayışı</li>
          <li>Pasek wieloklinowy</li>
        </ul>
        <img id="img" src="./pulley.jpg" alt="pulley system" />
        <p
          style="
            margin-left: 1.5em;
            position: relative;
            z-index: 2;
            color: white;
            font-weight: bold;
            font-family: Arial, Helvetica, sans-serif;
          "
        >
          1 Pc
        </p>
        <img id="iso" src="./iso.png" alt="iso" />
      </div>
      <div id="right">
        <h1></h1>
        <img id="eac" src="./eac.png" alt="EAC" />
      </div>
      <div id="front">
        <h1>
          <p>VECTOR</p>
        </h1>
        <p
          style="
            position: relative;
            z-index: 2;
            margin-top: 2em;
            font-weight: bold;
            font-family: Arial, Helvetica, sans-serif;
            margin-left: 1.5em;
            font-size: 0.8rem;
          "
        >
          SUGGESTIONS:
        </p>
        <ol>
          <li>
            UPON REMOVAL FROM CONTAINER
            <ol
              style="
                list-style: upper-alpha;
                font-size: 0.75rem;
                margin: 0;
                font-weight: normal;
              "
            >
              <li>
                DO NOT BEND OR FOLD THE BELT IN ANY RADIUS smaller than the
                smallest pulley in the drive.
              </li>
              <li>DO NOT TWIST, KINK, or otherwise mishandle this belt.</li>
            </ol>
          </li>
          <li>
            DURING INSTALLATION
            <ol
              style="
                list-style: upper-alpha;
                font-size: 0.75rem;
                margin: 0;
                font-weight: normal;
              "
            >
              <li>
                If the belt will not load into the pulley positions without
                force or prying, recheck procedures for proper slack to allow a
                smooth, unforced installation.
              </li>
            </ol>
          </li>
          <li>
            TENSION
            <ol
              style="
                list-style: upper-alpha;
                font-size: 0.75rem;
                margin: 0;
                font-weight: normal;
              "
            >
              <li>
                Due to the varying requirements of precision synchronous drives,
                belt tension should always be set according to car
                manufacturer's specifications.
              </li>
              <li>DO NOT OVER TENSION.</li>
              <li>
                Once properly tensioned, retensioning is usually not necessary,
                consult vehicle manufacturer's service manual.
              </li>
            </ol>
          </li>
        </ol>
        <img id="qr" src="./qr.png" alt="qr" />
      </div>
    </div>
  </body>
</html>
"""

css = """
:root {
  --width: 377.95275591px;
  --height: 529.13385827px;
  --img-height: 430.71496063178px;
  --img-width: 604.72440945px;
  --offset: 188.976377955px;
  --side-width: 56.692913386px;
  /* --side-width: 68.031496063px; */
  /* --side-width: 83.149606299px; */
  /* --side-width: 94.488188976px; */
  /* --side-width: 113.38582677px; */
  /* --side-width: 120.94488189px; */
  /* --side-width: 162.51968504px; */
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

#front {
  width: var(--width);
  height: var(--height);
  background-color: red;
  /* display: flex; */
  position: relative;
  /* border: 1px solid; */
}

#front ul {
  list-style: none;
  margin: 2em 1.5em;
  color: white;
  font-weight: bolder;
  font-family: Arial, Helvetica, sans-serif;
  position: relative;
  z-index: 2;
}

#front ol {
  margin: 2em 3em;
  font-size: 0.8rem;
  margin-top: 0.25em;
  color: white;
  font-weight: bolder;
  font-family: Arial, Helvetica, sans-serif;
  position: relative;
  z-index: 2;
}

#front ol li {
  margin-bottom: 1em;
  font-size: 0.75em;
}
#img {
  position: absolute;
  width: calc(calc(var(--width) + var(--side-width)) * 2);
  height: var(--img-height);
  align-self: flex-end;
  top: calc(var(--height) - var(--img-height));
  opacity: 0.35;
  z-index: 1;
  left: calc(-1 * var(--side-width));
  filter: blur(4px);
}

#iso {
  position: relative;
  z-index: 2;
  width: 80px;
  height: 80px;
  margin: 1em 1em;
}

#qr {
  width: 150px;
  height: 150px;
  position: relative;
  z-index: 2;
  display: block;
  margin-inline: auto;
}

#left,
#right {
  width: var(--side-width);
  height: 100%;
  background-color: red;
  height: var(--height);
  /* border: 1px solid; */
  display: flex;
  flex-direction: column;
}

#recycle-container {
  display: flex;
  flex-direction: column;
  gap: 1em;
  margin-top: auto;
  margin-bottom: 3em;
  align-self: center;
  position: relative;
  z-index: 2;
}

.recycle {
  width: calc(var(--side-width) * 0.44097222222087480709876954920053);
  height: calc(var(--side-width) * 0.44097222222087480709876954920053);
}

#right {
  right: -200px;
}

#eac {
  width: calc(var(--side-width) * 0.88194444444174961419753909840106);
  height: calc(var(--side-width) * 0.88194444444174961419753909840106);
  position: relative;
  z-index: 2;
  margin-top: auto;
  margin-inline: auto;
  margin-bottom: 2em;
}

h1 {
  width: 100%;
  margin-top: 0.5em;
  background-color: white;
  height: calc(var(--height) - var(--img-height) - 0.5em);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

h1 p {
  width: 170px;
  /* overflow: visible; */
  border: 6px solid;
  border-image: linear-gradient(to right, red, black);
  border-image-slice: 1;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  font-style: italic;
  font-family: Arial, Helvetica, sans-serif;
  position: relative;
  font-weight: bolder;
  text-align: center;
  font-size: 2.25rem;
  margin-left: auto;
  margin-right: 0.75em;
  /* letter-spacing: 0.65em; */
  z-index: 2;
  background: linear-gradient(to right, red, 40%, black);
  color: transparent;
  background-clip: text;
}

body {
  background-color: rgb(189, 189, 189);
  width: 100vw;
  height: 100vh;
}


"""


data = { 'html': html,
         'css': css,
         }

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

print("Your image URL is: %s"%image.json()['url'])
# https://hcti.io/v1/image/7ed741b8-f012-431e-8282-7eedb9910b32

