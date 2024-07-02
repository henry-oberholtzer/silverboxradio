import { PropsWithChildren, useEffect, useMemo } from "react";
import { useLocalStorage } from "../useLocalStorage";
import { AuthContext } from "./AuthContext";



const AuthProvider = (props: PropsWithChildren) => {
  const [user, setUser] = useLocalStorage("user", null);

  useEffect(() => {
    if (user != null && Date.parse(user.expiry) < Date.now()) {
      setUser(null)
    }
  }, [user, setUser])

  const value = useMemo(
    () => ({
      user,
      login: async (data: UserSchema) => {
        setUser(data);
      },
      logout: () => {
        setUser(null);
      },
    }),
    [user, setUser]
  );
  return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}



export { AuthProvider }
