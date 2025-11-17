'use client';

import { motion } from 'framer-motion';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { useAppStore } from '@/lib/store';
import { ShoppingCart, Plane, Car, Utensils, ShoppingBag, Sparkles } from 'lucide-react';

const categories = [
  { key: 'groceries' as const, label: 'Groceries', icon: ShoppingCart, placeholder: '500' },
  { key: 'travel' as const, label: 'Travel', icon: Plane, placeholder: '300' },
  { key: 'gas' as const, label: 'Gas', icon: Car, placeholder: '200' },
  { key: 'dining' as const, label: 'Dining', icon: Utensils, placeholder: '400' },
  { key: 'online_shopping' as const, label: 'Online Shopping', icon: ShoppingBag, placeholder: '600' },
];

interface CardInputFormProps {
  onSubmit?: () => void;
}

export default function CardInputForm({ onSubmit }: CardInputFormProps) {
  const { spend, updateSpendCategory } = useAppStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (onSubmit) {
      onSubmit();
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <Card className="glass border-purple-500/20 shadow-xl">
        <CardHeader>
          <CardTitle className="gradient-text text-3xl">Monthly Spending</CardTitle>
          <CardDescription className="text-muted-foreground">
            Enter your estimated monthly spending in each category
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {categories.map((category, index) => {
                const Icon = category.icon;
                return (
                  <motion.div
                    key={category.key}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="space-y-2"
                  >
                    <label className="text-sm font-medium flex items-center gap-2">
                      <Icon className="w-4 h-4 text-purple-400" />
                      {category.label}
                    </label>
                    <div className="relative">
                      <span className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground">
                        $
                      </span>
                      <Input
                        type="number"
                        placeholder={category.placeholder}
                        value={spend[category.key] || ''}
                        onChange={(e) =>
                          updateSpendCategory(category.key, parseFloat(e.target.value) || 0)
                        }
                        className="pl-8 bg-background/50 border-purple-500/30 focus:border-purple-500"
                        min="0"
                        step="0.01"
                      />
                    </div>
                  </motion.div>
                );
              })}
            </div>
            <div className="pt-4">
              <Button
                type="submit"
                className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white shadow-lg"
                size="lg"
              >
                <Sparkles className="w-4 h-4 mr-2" />
                Find Best Cards
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </motion.div>
  );
}

