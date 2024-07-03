type UserContext = {
  user: UserSchema | null;
  login: (data: UserLoginSchema) => void;
  logout: () => void;
  message: string | null;
  dismissMessage: () => void;
}
