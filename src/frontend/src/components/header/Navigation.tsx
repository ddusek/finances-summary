import React, { useContext } from 'react';
import styled from 'styled-components';
import { UserContext } from '../../context/user';
import NavigationItem from './NavigationItem';

const Container = styled.nav`
  display: flex;
  flex-direction: row;
  align-items: center;
`;

const Navigation: React.FC = () => {
  const user = useContext(UserContext);
  return (
    <Container>
      <NavigationItem link="/global-stocks" text="Global stocks" />
      {user.loggedIn && <NavigationItem link="/my-stocks" text="My stocks" />}
      {!user.loggedIn && (
        <NavigationItem link="/sign-up" text="Sign up" highlight />
      )}
    </Container>
  );
};

export default Navigation;
