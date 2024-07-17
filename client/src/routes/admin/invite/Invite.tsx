import { Container } from "@mantine/core"
import { InviteForm } from "./InviteForm"
import { InviteTable } from "./InviteTable"



const Invite = () => {

  return (
    <Container>
      <h1>Invite Dashboard</h1>
      <InviteForm/>
      <InviteTable />
    </Container>
  )

}

export { Invite }
