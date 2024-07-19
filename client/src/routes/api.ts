import Cookies from "universal-cookie";

const apiFactory = (host: string) => {
  return (endpoint: string) => {
    return (method: "GET" | "POST" | "DELETE") => {
        return async (
          routeParams: string | number | null = null,
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
                return null
              }
              const data = await response.json();
              const pagination = response.headers.get("X-Pagination")
              if (pagination) {
                const pages = JSON.parse(pagination)
                const pageObject = {
                  pagination: pages,
                  data: data
                }
                return pageObject
              }
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
// const usersBase = base("/users")
const login = base("login")("POST")
const register = base("register")("POST")
const invitesBase = base("invites")
// const logout = base("/logout")("POST")


const api = {
	login: (body: UserLoginSchema) => login(null, body),
  invites: {
    get: (params?: string) => invitesBase("GET")(params),
    delete: (id: number | string) => invitesBase("DELETE")("/" + id),
    post: (body: object) => invitesBase("POST")(null, body)
  },
  users: {
    register: (body: object) => register(null, body)
  }
};

export { api };
