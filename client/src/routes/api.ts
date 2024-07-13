import Cookies from "universal-cookie";

const apiFactory = (host: string) => {
  return (endpoint: string) => {
    return (method: "GET" | "POST") => {
        return async (
          routeParams: string | null = null,
          body: object | null = null
        ) => {
          let url = host + endpoint;
          const cookies = new Cookies()
          const headers: HeadersInit = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-CSRF-TOKEN": cookies.get("csrf_access_token")
          }

          const request: RequestInit = {
            method: method,
            headers: headers,
            credentials: 'include'
          }
          if (body) {
            request.body = JSON.stringify(body)
          }
          if (routeParams != null) {
            url = url + routeParams;
          }
          try {
            const response = await fetch(url, request);
            if (response.ok) {
              if (response.status === 204) {
                return
              }
              const data = await response.json();
              return data;
            } else if (response.status >= 400) {
              const data = await response.json();
              return data;
            } else {
              throw new Error(`ERROR: ${response.status}: ${response.statusText}`)
            }
          } catch (error) {
            console.error(error)
          }
        };
      }
    }
  }

const base = apiFactory(import.meta.env.VITE_BACKEND + "/")
// const users = base("/users")
const login = base("login")("POST")
const invitesBase = base("invites")
// const logout = base("/logout")("POST")


const api = {
	login: (body: UserLoginSchema) => login(null, body),
  invites: {
    get: () => invitesBase("GET")(),
    post: (body: InvitePostSchema) => invitesBase("POST")(null, body)
  }
};

export { api };
