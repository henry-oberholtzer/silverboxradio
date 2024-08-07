import { useState } from "react"
import { Button, Container, Paper, PasswordInput, TextInput, Title, Text } from "@mantine/core"
import { useDisclosure } from "@mantine/hooks"

const Register = () => {
  const [username, setUsername] = useState<string>("")
  const [password, setPassword] = useState<string>("")
  const [confirmPassword, setConfirmPassword] = useState<string>("")
  const [visible, { toggle }] = useDisclosure(false);

  return (
    <Container>
      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <form>
          <Title order={2}>Register</Title>
          <Text>You must have an active invite from the admin to register.</Text>
          <TextInput
            label="Username"
            value={username}
            maxLength={30}
            description="May only contain letters, numbers and underscores."
            required
            onChange={(e) => setUsername(e.target.value)}
          />
          <PasswordInput
            mt="md"
            label="Password"
            value={password}
            description="At least 8 characters, one number, and one special character (!, @, #, $, %, ^, &, *)."
            required
            onChange={(e) => setPassword(e.target.value)}
            visible={visible}
            onVisibilityChange={toggle}
          />
          <PasswordInput
            mt="md"
            label="Confirm Password"
            value={confirmPassword}
            required
            onChange={(e) => setConfirmPassword(e.target.value)}
            visible={visible}
            onVisibilityChange={toggle}
          />
          <Button type="submit" fullWidth mt="xl">
            Login
          </Button>
        </form>
      </Paper>
    </Container>
  )
}

export { Register }
