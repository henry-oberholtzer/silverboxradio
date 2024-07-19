import { Table, Anchor, Pagination } from "@mantine/core"
import { useEffect } from "react"
import { useFetcher, useSearchParams} from "react-router-dom"
import { InviteDeleteButton } from "./InviteDeleteButton"

const InviteTable = () => {
  const fetcher = useFetcher()
  const [searchParams, setSearchParams] = useSearchParams();

  useEffect(() => {
    if (fetcher.state === "idle" && !fetcher.data) {
      if (searchParams) {
        fetcher.load("/admin/invite?" + searchParams.toString())
      }
      else
      {
        fetcher.load("/admin/invite")
        
      }
    }
  }, [fetcher, searchParams])

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
        {fetcher.data && fetcher.data.data.map((i: InviteSchema) => {
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
    {fetcher.data && fetcher.data.pagination.total_pages > 1 &&
    <Pagination
      total={fetcher.data.pagination.total_pages}
      value={fetcher.data.pagination.page}
      onChange={(value) => {
        setSearchParams([["page", `${value}`]]) 
        fetcher.load(`/admin/invite?page=${value}`)
      }}
    />}
  </Table.ScrollContainer>
  )
}

export { InviteTable }
