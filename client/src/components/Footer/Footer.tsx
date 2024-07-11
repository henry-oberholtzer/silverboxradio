import { Text, Container} from '@mantine/core';
import { SilverBoxRadio } from '../SilverBoxRadio';
import classes from './Footer.module.css'

const data = [
  {
    title: 'Program',
    links: [
      { label: 'Schedule', link: '/schedule'},
      { label: 'Shows', link: '/shows'},
      { label: 'Episodes', link: '/episodes'}
    ]
  },
  {
    title: 'About',
    links: [
      { label: 'Story', link: '/story' }
    ]
  },
  {
    title: 'Hosts',
    links: [
      { label: 'Hosts', link: '/hosts' },
      { label: 'DJ Login', link: '/login' },
    ]
  }
]

const Footer = () => {
  const groups = data.map((group) => {
    const links = group.links.map((link, index) => (
      <Text<'a'>
        key={index}
        className={classes.link}
        component="a"
        href={link.link}
      >
        {link.label}
      </Text>
    ))

    return (
      <div className={classes.wrapper} key={group.title}>
        <Text className={classes.title}>{group.title}</Text>
        {links}
      </div>
    )
  })

  return (
    <footer className={classes.footer}>
      <Container className={classes.inner}>
        <div className={classes.logo}>
          <SilverBoxRadio scale={80} />
          <Text size="xs" c="dimmed" className={classes.description}>
            Internet Radio Platform
          </Text>
        </div>
        <div className={classes.groups}>{groups}</div>
      </Container>
      <Container className={classes.afterFooter}>
        <Text c="dimmed" size="dm">
          (c) Henry Oberholtzer 2024
        </Text>
      </Container>
    </footer>
  )
}

export { Footer }
