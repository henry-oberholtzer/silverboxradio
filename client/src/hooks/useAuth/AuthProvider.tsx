import { PropsWithChildren, useEffect, useMemo, useState } from "react";
import { useLocalStorage } from "../useLocalStorage";
import { AuthContext } from "./AuthContext";
import { useCookies } from "react-cookie";

const AuthProvider = (props: PropsWithChildren) => {
  const [user, setUser] = useLocalStorage("user", null);
  const [message, setMessage] = useState<string>("")
  const [,setCookie] = useCookies()

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
                const accessToken = response.headers.get('access_token_cookie')
                const refreshToken = response.headers.get('refresh_token_cookie')
                accessToken ?
                setCookie('access_token_cookie', accessToken) : ""
                refreshToken ?
                setCookie('refresh_token_cookie', refreshToken) : ""
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
        setUser(null);
      },
      dismissMessage: () => {
        setMessage("")
      }
    }),
    [user, setCookie, message, setMessage, setUser]
  );
  return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}



export { AuthProvider }
