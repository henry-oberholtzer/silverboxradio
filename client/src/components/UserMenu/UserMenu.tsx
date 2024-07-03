import { UnstyledButton, Menu, Group, Avatar, Text, rem } from "@mantine/core"
import cx from 'clsx';
import { useState } from "react"
import { useAuth } from "../../hooks";
import { IconChevronDown, IconLogout, IconSettings, IconRadio, IconUpload, IconCalendarMonth } from "@tabler/icons-react";
import classes from './UserMenu.module.css'

const UserMenu = () => {
  const { user } = useAuth()
  const [userMenuOpened, setUserMenuOpened] = useState(false);

  return (
    user && (
    <Menu
      width={260}
      position="bottom-end"
      transitionProps={{ transition: 'pop-top-right' }}
      onClose={() => setUserMenuOpened(false)}
      onOpen={() => setUserMenuOpened(true)}
      withinPortal
      
    >
      <Menu.Target>
        <UnstyledButton
          className={cx(classes.user, { [classes.userActive]: userMenuOpened })}
        >
          <Group gap={7}>
            <Avatar src={'./temp_pfp.jpg'} alt={user.username} radius="xl" size={20} />
            <Text fw={500} size="sm" lh={1} mr={3}>
              {user.username}
            </Text>
            <IconChevronDown style={{ width: rem(12), height: rem(12) }} stroke={1.5} />
          </Group>
        </UnstyledButton>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Label>Admin</Menu.Label>
          <Menu.Item
              leftSection={
                <IconCalendarMonth
                style={{ width: rem(16), height: rem(16) }} stroke={1.5}/>
              }
              disabled>
              Manage Schedule
              </Menu.Item>
        <Menu.Label>Programs</Menu.Label>
          <Menu.Item
            leftSection={
              <IconUpload
              style={{ width: rem(16), height: rem(16) }} stroke={1.5}/>
            }
            disabled>
            Add Show
            </Menu.Item>
          <Menu.Item
            leftSection={
              <IconRadio
              style={{ width: rem(16), height: rem(16) }} stroke={1.5}/>
            }
            disabled>
            Manage Shows
          </Menu.Item>
        <Menu.Label>Account</Menu.Label>
        <Menu.Item
          leftSection={
            <IconSettings
              style={{ width: rem(16), height: rem(16) }} stroke={1.5}/>
          }
          disabled>
            Settings
        </Menu.Item>
        <Menu.Item
          leftSection={
            <IconLogout
              style={{ width: rem(16), height: rem(16) }} stroke={1.5}/>
          }
          onClick={() => console.log("Clicked")}>
            Logout
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
    )
  )
}

export { UserMenu }
