'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { X } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import type { CardRecommendation } from '@/lib/types';
import { formatCurrency, formatPercentage } from '@/lib/formatting';

interface DetailedSavingsModalProps {
  card: CardRecommendation | null;
  isOpen: boolean;
  onClose: () => void;
}

export default function DetailedSavingsModal({
  card,
  isOpen,
  onClose,
}: DetailedSavingsModalProps) {
  if (!card) return null;

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50"
          />

          {/* Modal */}
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 20 }}
              className="glass border-purple-500/30 rounded-xl shadow-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto"
            >
              <Card className="border-0 bg-transparent">
                <CardHeader className="flex flex-row items-center justify-between pb-4">
                  <CardTitle className="text-2xl gradient-text">
                    {card.card_name} - Detailed Breakdown
                  </CardTitle>
                  <Button
                    variant="ghost"
                    size="icon"
                    onClick={onClose}
                    className="text-gray-400 hover:text-white"
                  >
                    <X className="w-5 h-5" />
                  </Button>
                </CardHeader>
                <CardContent className="space-y-6">
                  {/* Summary */}
                  <div className="grid grid-cols-3 gap-4">
                    <div className="p-4 bg-purple-500/10 rounded-lg border border-purple-500/20">
                      <p className="text-sm text-gray-400 mb-1">Monthly Rewards</p>
                      <p className="text-2xl font-bold text-green-400">
                        {formatCurrency(card.estimated_monthly_rewards)}
                      </p>
                    </div>
                    <div className="p-4 bg-purple-500/10 rounded-lg border border-purple-500/20">
                      <p className="text-sm text-gray-400 mb-1">Annual Rewards</p>
                      <p className="text-2xl font-bold text-green-400">
                        {formatCurrency(card.estimated_annual_rewards)}
                      </p>
                    </div>
                    <div className="p-4 bg-purple-500/10 rounded-lg border border-purple-500/20">
                      <p className="text-sm text-gray-400 mb-1">Reward Rate</p>
                      <p className="text-2xl font-bold text-purple-400">
                        {formatPercentage(card.reward_rate)}
                      </p>
                    </div>
                  </div>

                  {/* Category Breakdown */}
                  {card.cashback_breakdown && card.cashback_breakdown.length > 0 && (
                    <div>
                      <h3 className="text-lg font-semibold text-white mb-4">
                        Category Breakdown
                      </h3>
                      <Table>
                        <TableHeader>
                          <TableRow className="border-purple-500/20">
                            <TableHead className="text-purple-300">Category</TableHead>
                            <TableHead className="text-purple-300">Monthly Spend</TableHead>
                            <TableHead className="text-purple-300">Reward Rate</TableHead>
                            <TableHead className="text-purple-300">Monthly Rewards</TableHead>
                          </TableRow>
                        </TableHeader>
                        <TableBody>
                          {card.cashback_breakdown.map((item, index) => (
                            <TableRow
                              key={index}
                              className="border-purple-500/10"
                            >
                              <TableCell className="font-medium text-white">
                                {item.category}
                              </TableCell>
                              <TableCell className="text-gray-300">
                                {formatCurrency((item as any).spend || 0)}
                              </TableCell>
                              <TableCell className="text-purple-400 font-semibold">
                                {formatPercentage(item.rate)}
                              </TableCell>
                              <TableCell className="text-green-400 font-semibold">
                                {formatCurrency(item.amount)}
                              </TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </div>
                  )}

                  {/* Annual Fee Info */}
                  <div className="p-4 bg-background/50 rounded-lg border border-purple-500/20">
                    <div className="flex items-center justify-between">
                      <span className="text-gray-400">Annual Fee</span>
                      <span
                        className={`font-semibold ${
                          card.annual_fee > 0 ? 'text-red-400' : 'text-green-400'
                        }`}
                      >
                        {card.annual_fee > 0
                          ? formatCurrency(card.annual_fee)
                          : 'No Annual Fee'}
                      </span>
                    </div>
                    {card.annual_fee > 0 && (
                      <div className="mt-2 pt-2 border-t border-purple-500/20 flex items-center justify-between">
                        <span className="text-gray-400">Net Annual Value</span>
                        <span className="font-bold text-green-400">
                          {formatCurrency(
                            card.estimated_annual_rewards - card.annual_fee
                          )}
                        </span>
                      </div>
                    )}
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </>
      )}
    </AnimatePresence>
  );
}


