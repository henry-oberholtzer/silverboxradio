import { PropsWithChildren, useEffect, useMemo, useState } from "react";
import { useLocalStorage } from "../useLocalStorage";
import { AuthContext } from "./AuthContext";
import Cookies from "universal-cookie";

const AuthProvider = (props: PropsWithChildren) => {
  const [user, setUser] = useLocalStorage("user", null);
  const [, setRefreshToken] = useLocalStorage("refresh_token_cookie", null)
  const [message, setMessage] = useState<string>("")

  useEffect(() => {
    if (user != null && Date.parse(user.expiry) < Date.now()) {
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
              headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
              },
              body: JSON.stringify(data)
            }).then(response => {
              if (response.ok) {
                const cookies = new Cookies()
                const accessToken = response.headers.get('access_token_cookie')
                const refreshToken = response.headers.get('refresh_token_cookie')
                cookies.set("access_token_cookie", accessToken, {
                  path: "/",
                  httpOnly: true,
                }) 
                refreshToken ? setRefreshToken(refreshToken) : ""
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
        try {
          await fetch(`${import.meta.env.VITE_BACKEND}/logout`, {
            method: "POST",
            credentials: "include",
            headers: {
              "Content-Type": "application/json",
              "Accept": "application/json"
            },
          }).then(response => {
            if (response.ok) {
              setUser(null)
              console.log("Logged out.")
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
    [user, message, setMessage, setUser, setRefreshToken]
  );
  return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}



export { AuthProvider }
