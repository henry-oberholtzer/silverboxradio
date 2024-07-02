import { PropsWithChildren, useEffect, useState } from "react"
import { ThemeProvider } from "styled-components"
import { BaseTheme } from "./themes"

const CustomThemeProvider = (props: PropsWithChildren) => {
  const [theme, setTheme] = useState<Theme>(BaseTheme)

  useEffect(() => {
    
    const adjustTheme = (e: MediaQueryListEvent) => {
      if (e.matches) {
        setTheme(BaseTheme)
      } else {
        setTheme(BaseTheme)
      }
    }


    window.matchMedia('(prefers-color-scheme: dark)').addEventListener("change", adjustTheme)
  }, [setTheme])

  return (
    <ThemeProvider theme={theme}>
      {props.children}
    </ThemeProvider>
  )
}

export { CustomThemeProvider }
