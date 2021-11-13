import React from 'react';

export interface User {
  loggedIn: boolean;
  username: string;
}

const initialUser: User = { loggedIn: false, username: '' };

const UserContext = React.createContext<User>(initialUser);

export { UserContext, initialUser };
