type UserContext = {
  user: UserSchema | null;
  login: (data: UserSchema) => void;
  logout: () => void;
}
