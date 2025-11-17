import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Research Agent Pro - AI Research with Auto Visualizations',
  description: 'The most sophisticated AI research agent with automatic charts, graphs, and infographics. Better than Perplexity and ChatGPT.',
  keywords: ['AI research', 'automatic charts', 'data visualization', 'AI agent', 'research tool'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
