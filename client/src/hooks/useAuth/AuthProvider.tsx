import { PropsWithChildren, useEffect, useMemo, useState } from "react";
import { useLocalStorage } from "../useLocalStorage";
import { AuthContext } from "./AuthContext";
import Cookies from "universal-cookie";

const AuthProvider = (props: PropsWithChildren) => {
  const [user, setUser] = useLocalStorage("user", null);
  const [message, setMessage] = useState<string>("")

  useEffect(() => {
    const cookies = new Cookies()
    console.log(cookies.get("access"))
    if (!cookies.get("access")) {
      setUser(null)
    }
  }, [user, setUser])

  const value = useMemo(
    () => ({
      user,
      message,
      login: async (data: UserLoginSchema) => {
        try {
            await fetch(`${import.meta.env.VITE_BACKEND}/login`, {
              method: "POST",
              credentials: "include",
              headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
              },
              body: JSON.stringify(data),
            }).then(response => {
              if (response.ok) {
                response.json().then(data => setUser(data))
              }
              if (response.status === 401) {
                setMessage("Incorrect username or password.")
              }
            })
          } catch (error) {
            console.error(error)
          }
      },
      logout: async () => {
        const cookies = new Cookies()
        try {
          const options: RequestInit = {
            method: "POST",
            credentials: "include",
            headers: {
              'X-CSRF-TOKEN': cookies.get("csrf_access_token")
            },
          }
          await fetch(`${import.meta.env.VITE_BACKEND}/logout`, options)
          .then(response => {
            if (response.ok) {
              cookies.remove("access")
              setUser(null)
            }
          })
        }
        catch (error) {
          console.error()
        }
      },
      dismissMessage: () => {
        setMessage("")
      }
    }),
    [user, message, setMessage, setUser,]
  );
  return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}



export { AuthProvider }
