import React from 'react';

export interface Responsivity {
  isMobile: boolean;
  isTablet: boolean;
  isDesktop: boolean;
}

const responsivity: Responsivity = {
  isMobile: false,
  isTablet: false,
  isDesktop: true,
};

const ResponsivityContext = React.createContext<Responsivity>(responsivity);

export { ResponsivityContext, responsivity };
