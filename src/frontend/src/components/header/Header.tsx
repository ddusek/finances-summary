import React from 'react';
import styled from 'styled-components';
import { COLOR_DARK } from '../../utils/cssConstants';
import { Navigation } from './Navigation';
import Logo from './Logo';

const Container = styled.div`
  background-color: ${COLOR_DARK};
  height: 60px;
  display: flex;
`;

const Header = () => {
  return (
    <Container>
      <Logo />
      <Navigation />
    </Container>
  );
};

export default Header;
