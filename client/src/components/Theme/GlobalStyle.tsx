import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
*, *::before, &::after {
  box-sizing: border-box;
  
}
@font-face {
  font-family: "Inter";
  src: url("./fonts/Inter_Variable.TTF") format("truetype");
}
* {
margin: 0;
}
body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
img,picture,video,canvas,svg {
  display: block;
  max-width: 100%;
}
input,button,textarea,select {
  font: inherit;
}
p,h1,h2,h3,h4,h5,h6 {
overflow-wrap: break-word;
}
p,h1,h2,h3,h4,h5,h6,a,button,input,textarea,select,label {
  font-family: "Inter", sans-serif;
}
#root, #__next {
isolation: isolate;
}`

export { GlobalStyle }
