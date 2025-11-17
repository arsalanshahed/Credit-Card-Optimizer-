'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { CreditCard, Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

const navItems = [
  { href: '/', label: 'Home' },
  { href: '/optimizer', label: 'Optimizer' },
  { href: '/dashboard', label: 'Dashboard' },
];

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav className="sticky top-0 z-50 glass-dark border-b border-purple-500/20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <Link href="/" className="flex items-center space-x-2 group">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
            >
              <CreditCard className="w-8 h-8 text-purple-400" />
            </motion.div>
            <span className="text-xl font-bold gradient-text">Card Optimizer</span>
          </Link>

          <div className="hidden md:flex items-center space-x-1">
            {navItems.map((item) => {
              const isActive = pathname === item.href;
              return (
                <Link key={item.href} href={item.href}>
                  <Button
                    variant={isActive ? 'default' : 'ghost'}
                    className={cn(
                      isActive && 'bg-gradient-to-r from-purple-600 to-pink-600'
                    )}
                  >
                    {item.label}
                  </Button>
                </Link>
              );
            })}
          </div>

          <Link href="/optimizer">
            <Button className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700">
              <Sparkles className="w-4 h-4 mr-2" />
              Get Started
            </Button>
          </Link>
        </div>
      </div>
    </nav>
  );
}


