import { SilverBoxRadio } from "../SilverBoxRadio"
import classes from './Header.module.css'
import { Container, Group, Burger } from "@mantine/core"
import { useDisclosure } from "@mantine/hooks"
import { Link } from "react-router-dom"
import { UserMenu } from "../UserMenu"

const links = [
  { link: '/schedule', label: 'Schedule'},
  { link: '/hosts', label: 'Hosts'},
  { link: '/about', label: 'About'},
]

const Header = () => {

  const [opened, { toggle }] = useDisclosure(false);

  const items = links.map((link) => (
    <Link
      key={link.label}
      to={link.link}
      className={classes.link}
    >
      {link.label}
    </Link>
  ))

  return (
    <header className={classes.header}>
      <Container size="md" className={classes.inner}>
        <SilverBoxRadio/>
        <Group gap={5} visibleFrom="sm">
          {items}
          <UserMenu/>
        </Group>
        <Burger opened={opened} onClick={toggle} size="sm" hiddenFrom="sm" />
      </Container>
    </header>

  )
}

export { Header }
