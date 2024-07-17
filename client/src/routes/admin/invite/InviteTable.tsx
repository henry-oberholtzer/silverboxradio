import { Table, Anchor } from "@mantine/core"
import { useEffect } from "react"
import { useFetcher } from "react-router-dom"
import { InviteDeleteButton } from "./InviteDeleteButton"

const InviteTable = () => {
  const fetcher = useFetcher()

  useEffect(() => {
    if (fetcher.state === "idle" && !fetcher.data) {
      fetcher.load("/admin/invite")
    }
  }, [fetcher])

  return (
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
          <Table.Th>
            Delete
          </Table.Th>
        </Table.Tr>
      </Table.Thead>
      <Table.Tbody>
        {fetcher.data && fetcher.data.map((i: InviteSchema) => {
          const date = new Date(i.created).toLocaleDateString()

          return (
            <Table.Tr key={i.email}>
              <Table.Td>
                <Anchor>
                  {i.email}
                </Anchor>
              </Table.Td>
              <Table.Td>
                {date}
              </Table.Td>
              <Table.Td>
                {i.owner.username}
              </Table.Td>
              <Table.Td>
                <InviteDeleteButton id={i.id}/>
              </Table.Td>
            </Table.Tr>
          )
        })}
      </Table.Tbody>
    </Table>
  </Table.ScrollContainer>

  )
}

export { InviteTable }
