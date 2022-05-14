import { useContext } from 'react';
import styled from 'styled-components';
import { UserContext } from '../../context/User';

const Container = styled.div`
  margin: 10px 0 0 10px;
  display: flex;
  margin-right: auto;
`;

export const NavigationUser = () => {
  const user = useContext(UserContext);
  return (
    <Container>
      <span>{user.username}</span>
    </Container>
  );
};
