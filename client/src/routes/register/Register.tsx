import { useState, useEffect } from "react"
import { IconX, IconCheck } from "@tabler/icons-react"
import { useNavigate } from "react-router-dom"
import { Button, Container, Paper, PasswordInput, TextInput, Title, Text, rem, Box, Progress } from "@mantine/core"
import { useDisclosure } from "@mantine/hooks"
import { api } from "../api"

const requirements = [
  { re: /[0-9]/, label: 'Includes number' },
  { re: /[a-z]/, label: 'Includes lowercase letter' },
  { re: /[A-Z]/, label: 'Includes uppercase letter' },
  { re: /[!@#$%^&*]/, label: 'Includes !, @, #, $, %, ^, & or *' },
  { re: /.{8,}/, label: 'At least 8 characters'}
];

const PasswordRequirement = ({ meets, label} : { meets: boolean, label: string}) => {
  return (
    <Text
      c={meets ? 'teal' : 'red'}
      style={{ display: 'flex', alignItems: 'center'}}
      mt={7}
      size="sm"
    >
      {meets ? (
        <IconCheck style={{ width: rem(14), height: rem(14)}} />
      ) : (
        <IconX style={{ width: rem(14), height: rem(14) }} />
      )}{'  '}
      <Box ml={10}>{label}</Box> 
    </Text>
  )
}

const getStrength = (password: string) => {
  let multiplier = password.length > 8 ? 0 : 1;

  requirements.forEach((req) => {
    if (!req.re.test(password)) {
      multiplier += 1;
    }
  })

  return Math.max(100 - (100 / (requirements.length + 1)) * multiplier, 10);
}

const Register = () => {
  const [username, setUsername] = useState<string>("")
  const [email, setEmail] = useState<string>("")
  const [password, setPassword] = useState<string>("")
  const [confirmPassword, setConfirmPassword] = useState<string>("")
  const [visible, { toggle }] = useDisclosure(false);
  const [usernameValidation, setUsernameValidation] = useState<boolean | null>(null)
  const [passwordMatch, setPasswordMatch] = useState<boolean>(false)
  const [passwordValidation, setPasswordValidation] = useState<boolean>(false)
  const [formValidation, setFormValidation] = useState<boolean>(false)
  const [usernameErrorMessage, setUsernameErrorMessage] = useState<string>("")
  const [emailErrorMessage, setEmailErrorMessage] = useState<string>("")
  const navigate = useNavigate()

// Sets password validation state
  useEffect(() => {
    if (getStrength(password) === 100) {
      setPasswordValidation(true)
    }
    if (password && confirmPassword) {
      if (password === confirmPassword) {
        setPasswordMatch(true)
      }
      else
      {
        setPasswordMatch(false)
      }
    }
  }, [password, confirmPassword])

// Sets username validation state
  useEffect(() => {
    if (username) {
      if (username.match(/\w+/g)) {
        setUsernameValidation(true)
      }
      else
      {
        setUsernameValidation(false)
      }
    }
    else
    {
      setUsernameValidation(null)
    }
  }, [username])

// Sets overall validation
  useEffect(() => {
    if (usernameValidation && passwordValidation && passwordMatch) {
      setFormValidation(true)
    }
    else
    {
      setFormValidation(false)
    }
  }, [usernameValidation, passwordValidation, passwordMatch])
  
  const strength = getStrength(password)
  const checks = requirements.map((requirement, index) => (
    <PasswordRequirement key={index} label={requirement.label} meets={requirement.re.test(password)} />
  ));
  const color = strength === 100 ? 'teal' : strength > 50 ? 'yellow' : 'red';

  const handleRegisterFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    console.log("I am submitting the form")
    const registration = await api.users.register({
      username: username,
      password: password,
      email: email
    })
    if (registration.errors) {
      const errors = registration.errors.json
      if (errors.email) {
        setEmailErrorMessage(errors.email.join(" "))
      }
      else
      {
        setEmailErrorMessage("")
      }
      if (errors.username) {
        console.log(errors.username)
        setUsernameErrorMessage(errors.username.join(" "))
      }
      else
      {
        setUsernameErrorMessage("")
      }
    } else if (registration.created) {
      navigate("/auth/login")
    }
  }

  return (
    <Container>
      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <form onSubmit={handleRegisterFormSubmit}>
          <Title order={2}>Register</Title>
          <TextInput
            mt="md"
            label="Username"
            value={username}
            maxLength={30}
            description="May only contain letters, numbers and underscores."
            error={usernameErrorMessage
              ? usernameErrorMessage :
              usernameValidation === false
            }
            required
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextInput
            mt="md"
            label="Email"
            value={email}
            description="Must match the email invited by the admin"
            maxLength={255}
            error={emailErrorMessage}
            required
            onChange={(e) => setEmail(e.target.value)}
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
            style={{ input: passwordMatch === true ? "outline: 2px solid green;" : "" }}
          />
          <Progress color={color} value={strength} size={5} mb="xs" mt="md" />
          {checks}
          <PasswordRequirement label="Passwords match" meets={passwordMatch} />
          <Button type="submit" fullWidth mt="xl" disabled={!formValidation}>
            Register
          </Button>
        </form>
      </Paper>
    </Container>
  )
}

export { Register }
