import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { COLOR_DARK } from '../../constants';

const Container = styled.div`
  background-color: ${COLOR_DARK};
  height: 40px;
`;

const Header: React.FC = () => {
  return (
    <Container>
      <span>header</span>
      <Link to="/a">a link</Link>
      <Link to="/b">b link</Link>
    </Container>
  );
};

export default Header;
