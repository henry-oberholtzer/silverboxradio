import { useState, useEffect } from "react"
import {
  PasswordInput,
  TextInput,
  Button,
  Container,
  Paper,
  Alert,
} from "@mantine/core"
import { IconInfoCircle } from "@tabler/icons-react"
import { useAuth } from "../../hooks"
import { useNavigate } from "react-router-dom"

const Login = () => {
  const [username, setUsername] = useState<string>("")
  const [password, setPassword] = useState<string>("")
  const navigate = useNavigate()
  const { login, message, dismissMessage, user } = useAuth()

  const resetForm = () => {
    setPassword("")
    setUsername("")
  }

  useEffect(() => {
    if (user) {
      navigate("/")
    }
  }, [user])


  const handleFormSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (username && password) {
      const body: UserLoginSchema = {
        username: username,
        password: password,
      }
      login(body)
      resetForm()
      
    }
  }

  const icon = <IconInfoCircle />

  return (
    <Container size={420} my={40}>
      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <form onSubmit={handleFormSubmit}>
          <TextInput
            label="Username"
            value={username}
            required
            onChange={(e) => setUsername(e.target.value)}
          />
          <PasswordInput
            mt="md"
            label="Password"
            value={password}
            required
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button type="submit" fullWidth mt="xl">
            Login
          </Button>
        </form>
      </Paper>
      {message && (
        <Alert
          variant="light"
          color="red"
          title={message}
          icon={icon}
          mt={30}
          withCloseButton
          closeButtonLabel="Dismiss"
          onClose={() => dismissMessage()}
        />
      )}
    </Container>
  )
}

export { Login }
