import { Title, Text, Button, Container, Group } from "@mantine/core"
import { useNavigate } from "react-router-dom"

const Restricted = (props: RestrictedProps) => {
  const navigate = useNavigate()

  return (
    <Container>
      <Title>Restricted</Title>
      <Text c="dimmed" size="lg" ta="center">
        {props.text ? props.text : 
        "This page is only available to adminstrators. If you believe this has been in error, please contact the station manager."
        }
      </Text>
      <Group justify="center">
        <Button variant="subtle" size="md" onClick={() => navigate(-1)}>
          Return
        </Button>
      </Group>
    </Container>
  )
}

export { Restricted }
