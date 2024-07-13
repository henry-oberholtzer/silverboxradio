import { useState } from "react"
import { Container, Group, TextInput, Button } from "@mantine/core"
import { useLoaderData } from "react-router-dom"

const Invite = () => {
  const [emails, setEmails] = useState<string>("")
  const invites = useLoaderData()

  console.log(invites)

  const handleInviteSubmit = () => {

  }

  return (
    <Container>
      <h1>Invite Dashboard</h1>
      <form onSubmit={handleInviteSubmit} autoComplete="off">
        <Group>
          <TextInput
            placeholder="Email"
            autoComplete="off" 
            aria-label="Email"
            value={emails}
            required
            onChange={(e) => setEmails(e.target.value)}/>
          <Button>
            Invite
          </Button>
        </Group>
      </form>
    </Container>
  )

}

export { Invite }
