const header = { 'Content-Type': 'application/json', }

const apiFactory = (host: string) => {
  return (endpoint: string) => {
    return (method: string) => {
        return async (
          routeParams: string | null = null, 
          headers: HeadersInit = { 'Content-Type': 'application/json', },
          body: object | null = null
        ) => {
          let url = host + endpoint;
          const request: RequestInit = {
            method: method,
            headers: headers,
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
            } else if (response.status === 401 || response.status === 400) {
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
// const logout = base("/logout")("POST")


const api = {
	login: (body: UserLoginSchema) => login(null, header, body)
};

export { api };
