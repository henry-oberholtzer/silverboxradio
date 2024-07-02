import styled from "styled-components"
import { SilverBoxRadio } from "../SilverBoxRadio"

const HeaderElement = styled.header`
  background-color: silver;
  height: 64px;
  display: flex;
  align-items: center;`

const Header = () => {
  return (
    <HeaderElement>
      <SilverBoxRadio/>
    </HeaderElement>
  )
}

export { Header }
