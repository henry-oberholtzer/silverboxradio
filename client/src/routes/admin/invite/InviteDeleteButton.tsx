import { Button } from '@mantine/core'
import { IconTrash } from '@tabler/icons-react'
import { useFetcher } from 'react-router-dom'

const InviteDeleteButton = (props: InviteDeleteButtonProps) => {
  const fetcher = useFetcher()

  return (
    <fetcher.Form method="DELETE" action={`${props.id}`}>
      <Button variant="subtle" color="red" type="submit">
      <IconTrash color="red" />
      </Button>
    </fetcher.Form>
  )
}

export { InviteDeleteButton }
