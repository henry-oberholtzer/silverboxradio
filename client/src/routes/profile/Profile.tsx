import { useAuth } from "../../hooks"

const Profile = () => {
  const { user } = useAuth()

  return (
    <>
      {user && 
      <h1> This is the user profile page for {user.username}</h1>
      }
    </>
  )
}

export { Profile }
