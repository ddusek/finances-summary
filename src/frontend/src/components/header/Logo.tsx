import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
  margin: 10px 0 0 10px;
  display: flex;
  margin-right: auto;
`;

const Logo = () => {
  return (
    <Container>
      <Link to="/">Finances summary</Link>
    </Container>
  );
};

export default Logo;
