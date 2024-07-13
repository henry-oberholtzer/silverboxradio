import { useState } from "react"
import { Container, Group, TextInput, Button, Table, Anchor } from "@mantine/core"
import { useLoaderData } from "react-router-dom"
import { api } from "../../api"

const Invite = () => {
  const [emails, setEmails] = useState<string>("")
  const [message, setMessage] = useState<string>("")
  const invites = useLoaderData() as InviteSchema[]

  const handleInviteSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (emails) {
      const response = await api.invites.post({
        email: emails,
      })
      if (response.errors) {
        setMessage("Error")
      }
      else
      {

      }
    }
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
            name="email"
            value={emails}
            required
            onChange={(e) => setEmails(e.target.value)}/>
          <Button type="submit">
            Invite
          </Button>
        </Group>
      </form>
      <Table.ScrollContainer minWidth={800}>
        <Table verticalSpacing="sm">
          <Table.Thead>
            <Table.Tr>
              <Table.Th>
                Email
              </Table.Th>
              <Table.Th>
                Invited On
              </Table.Th>
              <Table.Th>
                Created By
              </Table.Th>
            </Table.Tr>
          </Table.Thead>
          <Table.Tbody>
            {invites && invites.map((i) => {
              return (
                <Table.Tr key={i.email}>
                  <Table.Td>
                    <Anchor>
                      {i.email}
                    </Anchor>
                  </Table.Td>
                  <Table.Td>
                    {i.created}
                  </Table.Td>
                  <Table.Td>
                    {i.owner.username}
                  </Table.Td>
                </Table.Tr>
              )
            })}
          </Table.Tbody>
        </Table>
      </Table.ScrollContainer>

    </Container>
  )

}

export { Invite }
