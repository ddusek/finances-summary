import React from 'react';
import styled from 'styled-components';
import NavigationItem from './NavigationItem';

const Container = styled.nav`
  display: flex;
  flex-direction: row;
  align-items: center;
`;

const Navigation: React.FC = () => {
  return (
    <Container>
      <NavigationItem link="/global-stocks" text="Global stocks" />
      <NavigationItem link="/my-stocks" text="My stocks" />
      <NavigationItem link="/sign-up" text="Sign up" highlight />
    </Container>
  );
};

export default Navigation;
